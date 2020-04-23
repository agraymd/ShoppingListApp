// Sets list equal to the ol with id groceryList
var list = document.getElementById("groceryList");

// Sets variable i to 0 for dynamically generating ID of li element
var i = 0

// Listens for enter button press to append item to list.
var groceryItemInput = document.getElementById("addItemText");
groceryItemInput.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("addItemBtn").click();
    }
})

function addItem(){

    // Sets groceryItem to the value with the text input on list page.
    var groceryItem = document.getElementById("addItemText").value;

    // Sets item as variable to create li item.
    var item = document.createElement("li");

    // Creates ID for item, adds i to for id='item[i]'
    item.setAttribute('id', 'item'+i);

    // Appends text of input field as child of li element.
    item.appendChild(document.createTextNode(groceryItem));

    // Adds li to ol element
    list.appendChild(item);

    // Creates variable for remove button next to list item
    var removeButton = document.createElement('button');

    // Adds remove item as text to button
    removeButton.appendChild(document.createTextNode("Remove Item"));

    // Removing item from list using removeButton and item ID, append button to li
    removeButton.setAttribute('onClick', 'removeItem("'+'item'+i+'")');
    item.appendChild(removeButton);
    i+=1 // Increments i for next ID assignment.

    // Reset text field to empty
    document.getElementById("addItemText").value = '';

    // Set focus back into text area.
    document.getElementById("addItemText").focus();
}

// Function to remove item from list using removeButton

function removeItem(itemid){
    var item = document.getElementById(itemid);
    list.removeChild(item);
}