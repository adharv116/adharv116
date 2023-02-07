/* 
1. show / hide button 
---------------------
*/
// create variables

const divList = document.querySelector('.listHolder');


/* 
2. add list items
-----------------
*/
// create variables
const addInput = document.querySelector('#addInput');
const addBtn = document.querySelector('#addBtn');
const todosContainer = document.querySelector('.todos-container');

function addLists() {
  if (addInput.value === '') {
    alert('Enter the list name please!!!');
  } else {
    const ul = divList.querySelector('ul');
    const li = document.createElement('li');
    li.innerHTML = addInput.value;
    addInput.value = '';
    ul.appendChild(li);
    createBtn(li);
  }
}


// add list when clicked on add item button
addBtn.addEventListener('click', () => {
  addLists();
});

// add list when pressed enter
addInput.addEventListener('keyup', (event) => {
  if(event.which === 13) {
    addLists();
  }
});

// create p element add id = todo-text
const todoText = document.createElement('p');
todoText.id = 'todo-text';
todoText.innerText = addInput.value;


/* 
3. create action buttons
------------------------
*/
// create variables
const listUl = document.querySelector('.list');
const lis = listUl.children;

function createBtn(li) {
  // create remove button
  const remove = document.createElement('button');
  remove.className = 'btn-icon remove';
  li.appendChild(remove);

  // create button add id= edit=button
  const editButton = document.createElement('button');
  editButton.id = 'edit-button';
  // create img add to edit button
  const editImage = document.createElement('img');
  editImage.src = 'edit.svg';
  editButton.appendChild(editImage);
  li.appendChild(editButton);

  //  add click event to edit-button here
editButton.addEventListener('click', () => {
  addInput.value = todoText.innerText;
  const parent = editButton.parentElement;
  parent.parentElement.removeChild(parent);
});

  
  // create down button
  const down = document.createElement('button');
  down.className = 'btn-icon down';
  li.appendChild(down);

  


  // create up button
  const up = document.createElement('button');
  up.className = 'btn-icon up';
  li.appendChild(up);

  

  return li;
}

// loop to add buttons in each li
for (var i = 0; i < lis.length; i++) {
  createBtn(lis[i]);
}


/* 
4. enabling button actions (to move item up, down or delete)
------------------------------------------------------------
*/


divList.addEventListener('click', (event) => {
  if (event.target.tagName === 'BUTTON') {
    const button = event.target;
    const li = button.parentNode;
    const ul = li.parentNode;
    if (button.className === 'btn-icon remove') {
      ul.removeChild(li);

  

    
    
    } else if (button.className === 'btn-icon down') {
      const nextLi = li.nextElementSibling;
      if (nextLi) {
        ul.insertBefore(nextLi, li);
      }
    } else if (button.className === 'btn-icon up') {
      const prevLi = li.previousElementSibling;
      if (prevLi) {
        ul.insertBefore(li, prevLi);
      }
    }
  }
});