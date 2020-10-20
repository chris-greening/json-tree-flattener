let Node = require('./node.js')

class Tree {
    constructor(jsonDict) {
        this.jsonDict = jsonDict;
        this.mapTree(this.jsonDict);
    }

    mapTree(jsonDict) {
        this.leafNodes = [];
        this.rootNode = Node(jsonData, tree=this);
    }
}

module.exports = Tree