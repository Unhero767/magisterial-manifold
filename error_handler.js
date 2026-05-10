
// errorHandler.js - Centralized error handling
class ErrorHandler {
    constructor(config) {
        this.config = config;
        this.errorLog = [];
        this.setupGlobalErrorHandling();
    }

    setupGlobalErrorHandling() {
        window.addEventListener('error', (event) => {
            this.handleError(event.error, 'global');
        });

        window.addEventListener('unhandledrejection', (event) => {
            this.handleError(event.reason, 'promise');
        });
    }

    handleError(error, context = 'unknown') {
        const errorInfo = {
            message: error.message || 'Unknown error',
            stack: error.stack,
            context: context,
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent
        };

        this.errorLog.push(errorInfo);

        if (this.config.get('debug.enableLogging')) {
            console.error('Error occurred:', errorInfo);
        }

        // Notify user of error (non-blocking)
        this.showErrorToUser(errorInfo);
    }

    showErrorToUser(errorInfo) {
        // Create non-intrusive error notification
        const notification = document.createElement('div');
        notification.className = 'error-notification';
        notification.innerHTML = `
            <div class="error-content">
                <span class="error-icon">⚠️</span>
                <span class="error-message">Something went wrong. Please try again.</span>
                <button class="error-dismiss" onclick="this.parentElement.parentElement.remove()">×</button>
            </div>
        `;

        document.body.appendChild(notification);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, 5000);
    }

    // Wrapper for async operations
    async safeAsync(asyncFn, fallback = null) {
        try {
            return await asyncFn();
        } catch (error) {
            this.handleError(error, 'async');
            return fallback;
        }
    }

    // Wrapper for sync operations
    safeSync(syncFn, fallback = null) {
        try {
            return syncFn();
        } catch (error) {
            this.handleError(error, 'sync');
            return fallback;
        }
    }

    getErrorLog() {
        return [...this.errorLog];
    }

    clearErrorLog() {
        this.errorLog = [];
    }
}
