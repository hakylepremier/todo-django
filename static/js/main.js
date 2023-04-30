const dropDownBtn = document.querySelectorAll('.todo-more-btn');
const dropDownMenu = document.querySelectorAll('.todo-more-menu');
const doneBtn = document.querySelectorAll('.todo-done-container')
const todoItem = document.querySelectorAll('.todo-item')


dropDownBtn.forEach((e,i)=>{
  e.addEventListener('click',()=>{
    dropDownMenu[i].classList.toggle('todo-more-menu-enable')
  })
})

doneBtn.forEach((e,i)=>{
  e.addEventListener('click', ()=>{
    todoItem[i].classList.toggle('todo-done-checked')
  })
})
