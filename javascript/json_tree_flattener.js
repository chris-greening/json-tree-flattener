let jsonDict =  require('../test.json');
let Tree = require('./tree.js')

class JsonTreeFlattener {
    constructor(jsonDict){
        this.jsonDict = jsonDict;

        this.jsonTree = new Tree(this.jsonDict);
    }
}

const test = new JsonTreeFlattener(jsonDict);

// console.log(test.jsonTree.leafNodes);

for (i=0; i<test.jsonTree.leafNodes.length; i++) {
    console.log(test.jsonTree.leafNodes[i].jsonData);
}