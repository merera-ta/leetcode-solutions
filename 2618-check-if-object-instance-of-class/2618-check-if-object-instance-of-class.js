function checkIfInstanceOf(obj, classFunction) {
    if (obj == null || classFunction == null) {
        return false;
    }

    let proto = Object.getPrototypeOf(Object(obj));

    while (proto !== null) {
        if (proto === classFunction.prototype) {
            return true;
        }

        proto = Object.getPrototypeOf(proto);
    }

    return false;
}