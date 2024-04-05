/* Problem
Given the root of a binary tree, invert the tree, and return its root.
Example 
input: root = [4,2,7,1,3,6,9]
Expected Output: [4, 7, 2, 9, 6, 3, 1]
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */

var invertTree = (root) => {
   if (!root) return null;

   const queue = [root];

   while(queue.length) {
    const queueLength = queue.length;

    for (let i = 0; i < queueLength; i++) {
        const current = queue.shift()

        // Swap children 
        const temp = current.left;
        current.left = current.right;
        current.right = temp;

        // Push to the array 
        if (current.left) queue.push(current.left);
        if (current.right) queue.push(current.right);
    }
   }

   return root;
}