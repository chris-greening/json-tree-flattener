let jsonDict =  require('../test.json');
let Tree = require('./tree.js')

class JsonTreeFlattener {
    constructor(jsonDict){
        this.jsonDict = jsonDict;
    }
}

const test = new JsonTreeFlattener(jsonDict);

