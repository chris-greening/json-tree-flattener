class Node {
    constructor(jsonData, tree, linkedList=[], priorKeys=[]) {
        this.jsonData = jsonData;
        this.tree = tree;
        this.linkedList = linkedList;
        this.priorKeys = priorKeys;

        this.dtype = this._determineObjectType(this.jsonData);
        // console.log(this.dtype);
        this.nodes = []
        
        if (this.isLeaf) {
            var lastKey = this.priorKeys[this.priorKeys.length-1];
            var lastValue = this.jsonData;
            this.jsonData = {};
            this.jsonData[lastKey] = lastValue;
            this.tree.leafNodes.push(this);
        } else {
            this._getEdges()
        }
    }

    _determineObjectType(jsonData) {
        //determine if the object passed is an array
        if (typeof(jsonData) == "object") {
            if (Object.prototype.toString.call(jsonData) == "[object Object]") {
                var dtype = 'object';
            } else {
                var dtype = 'array';
            }
        } else {
            dtype = typeof(jsonData);
        }
        return dtype;
    }

    get isLeaf() {
        //Determine whether the node is a leaf node
        return ((this.dtype != 'object') && (this.dtype != 'array'));
    }

    _getEdges() {
        //Get edges to other nodes in tree recursively
        if (this.dtype == 'array') {
            for (i = 0; i < this.jsonData.length; i++) {
                var currentData = this.jsonData[i];

                //Construct references for the next Node
                var nextLinkedList = [...this.linkedList];
                var nextPriorKeys = [...this.priorKeys];
                nextLinkedList.push(this);
                nextPriorKeys.push(i);

                var newNode = new Node(currentData, this.tree, nextLinkedList, nextPriorKeys);
                this.nodes.push(newNode);
            }
        } else {
            for (var key of Object.keys(this.jsonData)) {
                var currentData = this.jsonData[key];

                //Construct references for the next Node
                var nextLinkedList = [...this.linkedList];
                var nextPriorKeys = [...this.priorKeys];
                nextLinkedList.push(this);
                nextPriorKeys.push(key);

                var newNode = new Node(currentData, this.tree, nextLinkedList, nextPriorKeys);
                this.nodes.push(newNode);
            }
        }
    }

    _getIterArr() {
        //Return an array that we will iterate over determined by this.dtype
        if (this.dtype == 'array') {

        }
    }
}

module.exports = Node;