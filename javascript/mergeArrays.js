function mergeArrays(arr1, arr2) {
    return [...arr1, ...arr2].sort((a, b) => a - b).reduce((c,d) => {
        if (!c.includes(d)){
            c.push(d)
        }

        return c;
    }, []);
}

module.exports =  mergeArrays;