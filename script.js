// array that holds the to-do items
let todoItems = [];

// Render the todo items
function renderTodo(todo) {
  // local storage, makes tasks persist even when the website is exited out of
  localStorage.setItem('todoItemsRef', JSON.stringify(todoItems));

  // select the first element with a class of 'js-todo-list'
  const list = document.querySelector('.js-todo-list');
  
  // select the current todo item in the DOM
  const item = document.querySelector(`[data-key='${todo.id}']`);

  // check if 'todo.checked' is true and if true, assign 'done' otherwise, assign an empty string
  const isChecked = todo.checked ? 'done' : '';
  
  // Create an `li` element and assign it to `node`
  const node = document.createElement('li');

  // set the class attribute
  node.setAttribute('class', `todo-item ${isChecked}`);

  // Set the data-key attribute to the id of the todo
  node.setAttribute('data-key', todo.id);

  // Set the contents of the `li` element created above
  node.innerHTML = `
    <input id="${todo.id}" type="checkbox"/>
    <label for="${todo.id}" class="tick js-tick"></label>
    <span>${todo.text}</span>
    <button class="delete-todo js-delete-todo">
    <svg><use href="#delete-icon"></use></svg>
    </button>
  `;

  // removes the item from the DOM
  if (todo.deleted) {
    item.remove();

    // clear whitespace from the list container
    // when `todoItems` is empty
    if (todoItems=== 0)
      list.innerHTML = '';
    return;
  }
  
  // if the item already exists in the DOM
  if (item) {
    // then replace it with whatever node has
    list.replaceChild(node, item);
  }

  else {
    // otherwise, append the element to the Document Object Model as the last child of the element referenced by the `list` variable
    list.append(node);
  }

};


// This function will create a new todo object based on the
// text that was entered in the text input, and push it into
// the `todoItems` array
function addTodo(text) {
  // a new todo object
  const todo = {
    text,
    checked: false,
    id: Date.now(),     // gets random id based on the Date.now() method (ms since 1/1/1970)
  };

  // pushes the todo object into the array
  todoItems.push(todo);
  
  // renders the todo object
  renderTodo(todo);
}

// This function recives the key of the list item that was checked or unchecked and finds the corresponding entry in the todoItems array using the findIndex method.
function toggleDone(key) {
  // findIndex() is a array method that returns the position of an element in the array
  const index = todoItems.findIndex(item => item.id === Number(key));

  // locate the todo item in todoItems[] and set its checked property to its opposite
  // i.e) true --> false, false --> true

  // to check and uncheck the "checked" status
  todoItems[index].checked = !todoItems[index].checked;

  // renders changes to the item (or task)
  renderTodo(todoItems[index]);
}

function deleteTodo(key) {
  // find the corresponding todo object in the todoItems array
  const index = todoItems.findIndex(item => item.id === Number(key));
  // create a new object with properties of the current todo item and a `deleted` property which is set to true
  const todo = {
    deleted: true,
    ...todoItems[index]
  };
  // remove the todo item from the array
  todoItems = todoItems.filter(item => item.id !== Number(key));
  // render changes to the item (or task)
  renderTodo(todo);
}

// select the form element
const form = document.querySelector('.js-form');

// Add a submit event listener
form.addEventListener('submit', event => {
  // prevent page refresh on form submission
  event.preventDefault();

  // select the text input
  const input = document.querySelector('.js-todo-input');

  // Get the value of the input and remove whitespace
  const text = input.value.trim();

  // if text isn't empty, then push the object onto the array
  if (text != '') {
    addTodo(text);
    input.value='';
    input.focus(); // focuses on the text input
  }
});

// selecting the entire list
const list = document.querySelector('.js-todo-list');
// add a event listener that listens for a "click" to the list and its children (tasks).
list.addEventListener('click', event => {
  // for completing tasks
  if (event.target.classList.contains('js-tick')) {
    // gets key id of each task (or node)
    const itemKey = event.target.parentElement.dataset.key;
    // when clicked on, should mark the item (task) as done
    toggleDone(itemKey);
  }

// for deleting tasks
if (event.target.classList.contains('js-delete-todo')) {
  const itemKey = event.target.parentElement.dataset.key;
  deleteTodo(itemKey);
}
});

// render any existing todo list items when the page is loaded
document.addEventListener('DOMContentLoaded', () => {
  // retrieve the value of todoItemsRef from the localStorage
  const ref = localStorage.getItem('todoItemsRef');
  if (ref) {
    // If it exists, the JSON.parse method is used to convert the JSON string back to its original array form and save it in todoItems.
    todoItems = JSON.parse(ref);
    todoItems.forEach(t => {
      renderTodo(t);
    });
  }
});
