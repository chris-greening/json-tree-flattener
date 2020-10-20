class Node {
    constructor(jsonData, tree, linkedList=[], priorKeys=[]) {
        this.jsonData = jsonData;
        this.tree = tree;
        this.linkedList = linkedList;
        this.priorKeys = this.priorKeys;

        this.dtype = _determineObjectType();

        if (this.isLeaf) {

        } else {
            this._getEdges()
        }


    }

    _determineObjectType() {
        //determine if the object passed is an array
        if (typeof (this.jsonData) == 'object') {
            if (this.jsonData.constructor == Object) {
                this.dtype = 'object';
            } else {
                this.dtype = 'array';
            }
        }
    }

    get isLeaf() {
        //Determine whether the node is a leaf node
        return ((this.dtype != 'object') && (this.dtype != 'array'));
    }

    _getEdges() {
        //Get edges to other nodes in tree recursively
        // var iterArr = ;
    }

    _getIterArr() {
        //Return an array that we will iterate over determined by this.dtype
        if (this.dtype == 'array') {

        }
    }
}

module.exports = Node;