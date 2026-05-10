
// config.js - Centralized configuration management
class ConfigManager {
    constructor() {
        this.config = {
            ui: {
                debounceDelay: 300,
                animationDuration: 300,
                maxCacheSize: 100,
                renderBatchSize: 10
            },
            game: {
                maxLevel: 20,
                minAbilityScore: 8,
                maxAbilityScore: 18,
                defaultProficiencyBonus: 2
            },
            performance: {
                enableCaching: true,
                enableLazyLoading: true,
                cacheTimeout: 300000, // 5 minutes
                maxMemoryUsage: 50 // MB
            },
            debug: {
                enableLogging: true,
                logLevel: 'info',
                enablePerformanceMonitoring: true
            }
        };
    }

    get(path) {
        return path.split('.').reduce((obj, key) => obj?.[key], this.config);
    }

    set(path, value) {
        const keys = path.split('.');
        const last = keys.pop();
        const target = keys.reduce((obj, key) => obj[key] = obj[key] || {}, this.config);
        target[last] = value;
    }

    validate() {
        // Validate configuration values
        const errors = [];

        if (this.get('ui.debounceDelay') < 0) {
            errors.push('UI debounce delay must be non-negative');
        }

        if (this.get('game.maxLevel') < 1) {
            errors.push('Max level must be at least 1');
        }

        return errors;
    }
}
