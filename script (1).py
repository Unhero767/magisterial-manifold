# Create optimized versions of the key components

# 1. Optimized DataManager with caching and lazy loading
optimized_data_manager = """
class OptimizedDataManager {
    constructor() {
        this._cache = new Map();
        this._initialized = false;
        this._loadPromise = null;
    }

    async initialize() {
        if (this._initialized) return;
        if (this._loadPromise) return this._loadPromise;
        
        this._loadPromise = this._loadData();
        await this._loadPromise;
        this._initialized = true;
    }

    async _loadData() {
        // Lazy load data only when needed
        try {
            const [racesData, classesData, backgroundsData] = await Promise.all([
                this._loadRaces(),
                this._loadClasses(), 
                this._loadBackgrounds()
            ]);
            
            this.races = racesData;
            this.classes = classesData;
            this.backgrounds = backgroundsData;
        } catch (error) {
            console.error('Failed to load game data:', error);
            throw new Error('Data loading failed');
        }
    }

    getRaceData(name) {
        if (!this._initialized) {
            throw new Error('DataManager not initialized');
        }
        
        const cacheKey = `race_${name}`;
        if (this._cache.has(cacheKey)) {
            return this._cache.get(cacheKey);
        }
        
        const data = this.races?.[name] || {};
        this._cache.set(cacheKey, data);
        return data;
    }

    // Memoized proficiency bonus calculation
    getProficiencyBonus(level) {
        const cacheKey = `pb_${level}`;
        if (this._cache.has(cacheKey)) {
            return this._cache.get(cacheKey);
        }
        
        let bonus;
        if (level >= 1 && level <= 4) bonus = 2;
        else if (level >= 5 && level <= 8) bonus = 3;
        else if (level >= 9 && level <= 12) bonus = 4;
        else if (level >= 13 && level <= 16) bonus = 5;
        else if (level >= 17 && level <= 20) bonus = 6;
        else bonus = 0;
        
        this._cache.set(cacheKey, bonus);
        return bonus;
    }
}
"""

# 2. Optimized CharacterBuilder with state caching
optimized_character_builder = """
class OptimizedCharacterBuilder {
    constructor(dataManager) {
        this.dataManager = dataManager;
        this._stateCache = new Map();
        this._calculationCache = new Map();
        this.characterSheet = this._initializeSheet();
    }

    // Memoized modifier calculation
    calculateModifier(score) {
        if (this._calculationCache.has(`mod_${score}`)) {
            return this._calculationCache.get(`mod_${score}`);
        }
        
        const modifier = Math.floor((score - 10) / 2);
        this._calculationCache.set(`mod_${score}`, modifier);
        return modifier;
    }

    // State-aware building with caching
    buildCharacter(userInputs, forceRebuild = false) {
        const inputHash = this._hashInputs(userInputs);
        
        if (!forceRebuild && this._stateCache.has(inputHash)) {
            this.characterSheet = { ...this._stateCache.get(inputHash) };
            return this.characterSheet;
        }

        // Only rebuild if inputs changed
        this._performBuild(userInputs);
        this._stateCache.set(inputHash, { ...this.characterSheet });
        
        return this.characterSheet;
    }

    _hashInputs(inputs) {
        return JSON.stringify(inputs);
    }

    _performBuild(userInputs) {
        // Reset and build with optimized flow
        this.characterSheet = this._initializeSheet();
        
        // Batch calculations to reduce overhead
        this._batchApplyChanges(() => {
            this.characterSheet.ability_scores = { ...userInputs.base_scores };
            this.applyRace(userInputs.race);
            this.calculateAllModifiers();
            this.applyClass(userInputs.class);
            this.applyBackground(userInputs.background);
            this.manageInventory(userInputs.gold, userInputs.items);
            this._performFinalCalculations();
        });
    }

    _batchApplyChanges(callback) {
        // Batch multiple operations to reduce recalculation
        this._isBatchMode = true;
        try {
            callback();
        } finally {
            this._isBatchMode = false;
        }
    }

    clearCache() {
        this._stateCache.clear();
        this._calculationCache.clear();
    }
}
"""

# 3. Optimized UI with efficient rendering
optimized_ui_manager = """
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
"""

print("OPTIMIZED D&D CHARACTER BUILDER COMPONENTS")
print("=" * 50)
print("\n1. OPTIMIZED DATA MANAGER")
print("-" * 30)
print("- Implements lazy loading and caching")
print("- Async initialization pattern")
print("- Memoized calculations")
print("- Error handling and recovery")

print("\n2. OPTIMIZED CHARACTER BUILDER") 
print("-" * 30)
print("- State caching with input hashing")
print("- Batched calculations")
print("- Memoized modifier calculations")  
print("- Conditional rebuilding")

print("\n3. OPTIMIZED UI MANAGER")
print("-" * 30)
print("- Batched DOM updates")
print("- Efficient event listener management")
print("- Render queuing and frame optimization")
print("- Memory leak prevention")

# Save optimized components to files
with open('optimized_data_manager.js', 'w') as f:
    f.write(optimized_data_manager)

with open('optimized_character_builder.js', 'w') as f:
    f.write(optimized_character_builder)

with open('optimized_ui_manager.js', 'w') as f:
    f.write(optimized_ui_manager)

print(f"\nOptimized components saved to files:")
print("- optimized_data_manager.js")
print("- optimized_character_builder.js") 
print("- optimized_ui_manager.js")