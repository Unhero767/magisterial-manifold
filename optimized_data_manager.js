
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
