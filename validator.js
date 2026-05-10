
// validator.js - Input validation and sanitization
class Validator {
    constructor() {
        this.rules = new Map();
        this.setupDefaultRules();
    }

    setupDefaultRules() {
        this.addRule('abilityScore', (value) => {
            const num = parseInt(value);
            return {
                isValid: !isNaN(num) && num >= 8 && num <= 18,
                message: 'Ability score must be between 8 and 18'
            };
        });

        this.addRule('required', (value) => ({
            isValid: value != null && value !== '',
            message: 'This field is required'
        }));

        this.addRule('positiveNumber', (value) => {
            const num = parseFloat(value);
            return {
                isValid: !isNaN(num) && num >= 0,
                message: 'Must be a positive number'
            };
        });

        this.addRule('string', (value, minLength = 0, maxLength = Infinity) => {
            const str = String(value);
            return {
                isValid: str.length >= minLength && str.length <= maxLength,
                message: `Must be between ${minLength} and ${maxLength} characters`
            };
        });
    }

    addRule(name, validatorFn) {
        this.rules.set(name, validatorFn);
    }

    validate(value, ruleName, ...args) {
        const rule = this.rules.get(ruleName);
        if (!rule) {
            throw new Error(`Validation rule '${ruleName}' not found`);
        }
        return rule(value, ...args);
    }

    validateObject(obj, schema) {
        const errors = [];

        for (const [key, rules] of Object.entries(schema)) {
            const value = obj[key];

            for (const rule of rules) {
                const result = this.validate(value, rule.name, ...rule.args || []);
                if (!result.isValid) {
                    errors.push({
                        field: key,
                        message: result.message,
                        value: value
                    });
                }
            }
        }

        return {
            isValid: errors.length === 0,
            errors: errors
        };
    }

    sanitizeInput(value, type = 'string') {
        switch (type) {
            case 'string':
                return String(value).trim().slice(0, 1000); // Limit length
            case 'number':
                const num = parseFloat(value);
                return isNaN(num) ? 0 : num;
            case 'integer':
                const int = parseInt(value);
                return isNaN(int) ? 0 : int;
            case 'boolean':
                return Boolean(value);
            default:
                return value;
        }
    }
}
