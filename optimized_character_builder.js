
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
