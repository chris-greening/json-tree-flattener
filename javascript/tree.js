let Node = require('./node.js')

class Tree {
    constructor(jsonDict) {
        this.jsonDict = jsonDict;
        this._mapTree(this.jsonDict);
    }

    _mapTree(jsonDict) {
        //Get edges to all Node's inside the Tree
        this.leafNodes = [];
        this.rootNode = Node(jsonData, tree=this);
    }
}

module.exports = Tree