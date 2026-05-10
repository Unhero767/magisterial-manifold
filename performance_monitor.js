
// performanceMonitor.js - Performance tracking and optimization
class PerformanceMonitor {
    constructor(config) {
        this.config = config;
        this.metrics = new Map();
        this.observers = [];
        this.setupMonitoring();
    }

    setupMonitoring() {
        if (!this.config.get('debug.enablePerformanceMonitoring')) return;

        // Memory usage monitoring
        if ('memory' in performance) {
            setInterval(() => {
                this.recordMetric('memory', {
                    used: performance.memory.usedJSHeapSize,
                    total: performance.memory.totalJSHeapSize,
                    limit: performance.memory.jsHeapSizeLimit
                });
            }, 5000);
        }

        // Performance observer for render times
        if ('PerformanceObserver' in window) {
            const observer = new PerformanceObserver((list) => {
                list.getEntries().forEach((entry) => {
                    this.recordMetric('render', {
                        name: entry.name,
                        duration: entry.duration,
                        startTime: entry.startTime
                    });
                });
            });

            observer.observe({ entryTypes: ['measure'] });
            this.observers.push(observer);
        }
    }

    startTimer(name) {
        performance.mark(`${name}-start`);
    }

    endTimer(name) {
        performance.mark(`${name}-end`);
        performance.measure(name, `${name}-start`, `${name}-end`);
    }

    recordMetric(category, data) {
        if (!this.metrics.has(category)) {
            this.metrics.set(category, []);
        }

        const metrics = this.metrics.get(category);
        metrics.push({
            ...data,
            timestamp: Date.now()
        });

        // Keep only recent metrics to prevent memory bloat
        if (metrics.length > 100) {
            metrics.shift();
        }
    }

    getMetrics(category) {
        return this.metrics.get(category) || [];
    }

    getAverageMetric(category, field) {
        const metrics = this.getMetrics(category);
        if (metrics.length === 0) return 0;

        const sum = metrics.reduce((acc, metric) => acc + (metric[field] || 0), 0);
        return sum / metrics.length;
    }

    generateReport() {
        const report = {
            timestamp: new Date().toISOString(),
            memory: {
                current: this.getMetrics('memory').slice(-1)[0],
                average: this.getAverageMetric('memory', 'used')
            },
            render: {
                averageDuration: this.getAverageMetric('render', 'duration'),
                totalRenders: this.getMetrics('render').length
            },
            recommendations: this.getRecommendations()
        };

        return report;
    }

    getRecommendations() {
        const recommendations = [];

        const avgMemory = this.getAverageMetric('memory', 'used');
        const maxMemory = this.config.get('performance.maxMemoryUsage') * 1024 * 1024;

        if (avgMemory > maxMemory) {
            recommendations.push('Memory usage is high. Consider clearing caches or optimizing data structures.');
        }

        const avgRenderTime = this.getAverageMetric('render', 'duration');
        if (avgRenderTime > 50) {
            recommendations.push('Render times are slow. Consider optimizing DOM operations or using virtual scrolling.');
        }

        return recommendations;
    }

    cleanup() {
        this.observers.forEach(observer => observer.disconnect());
        this.observers = [];
        this.metrics.clear();
    }
}
