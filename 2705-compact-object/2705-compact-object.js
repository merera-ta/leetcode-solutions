var compactObject = function(obj) {
    if (obj === null || typeof obj !== "object") {
        return obj;
    }

    if (Array.isArray(obj)) {
        return obj
            .filter(value => Boolean(value))
            .map(value => compactObject(value));
    }

    const result = {};

    for (const key in obj) {
        if (Boolean(obj[key])) {
            result[key] = compactObject(obj[key]);
        }
    }

    return result;
};