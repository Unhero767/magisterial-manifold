
class OptimizedUIManager {
    constructor(characterBuilder, dataManager) {
        this.cb = characterBuilder;
        this.dm = dataManager;
        this.currentStep = 1;
        this.userInputs = this._getDefaultInputs();
        this._renderQueue = [];
        this._isRendering = false;
        this._eventListeners = new Map();
    }

    // Efficient DOM updates with batching
    async renderStep() {
        if (this._isRendering) return;

        this._isRendering = true;

        try {
            // Queue render operations
            this._queueRender('progress', this._renderProgress.bind(this));
            this._queueRender('content', this._renderContent.bind(this));
            this._queueRender('buttons', this._renderButtons.bind(this));

            // Execute queued renders in single frame
            await this._flushRenderQueue();
        } finally {
            this._isRendering = false;
        }
    }

    _queueRender(key, renderFn) {
        this._renderQueue.push({ key, renderFn });
    }

    async _flushRenderQueue() {
        return new Promise(resolve => {
            requestAnimationFrame(() => {
                // Batch DOM updates
                const fragment = document.createDocumentFragment();

                this._renderQueue.forEach(({ renderFn }) => {
                    renderFn(fragment);
                });

                this._renderQueue = [];
                resolve();
            });
        });
    }

    // Efficient event listener management
    addEventListeners() {
        this._cleanupEventListeners();

        const listeners = [
            ['#next-btn', 'click', this._handleNext.bind(this)],
            ['#prev-btn', 'click', this._handlePrev.bind(this)],
            ['.progress-container', 'click', this._handleProgressClick.bind(this)]
        ];

        listeners.forEach(([selector, event, handler]) => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(el => {
                el.addEventListener(event, handler);
                this._eventListeners.set(el, { event, handler });
            });
        });
    }

    _cleanupEventListeners() {
        this._eventListeners.forEach(({ event, handler }, element) => {
            element.removeEventListener(event, handler);
        });
        this._eventListeners.clear();
    }

    // Debounced input handling
    _createDebouncedHandler(fn, delay = 300) {
        let timeoutId;
        return (...args) => {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => fn.apply(this, args), delay);
        };
    }

    destroy() {
        this._cleanupEventListeners();
        this.cb.clearCache();
    }
}
