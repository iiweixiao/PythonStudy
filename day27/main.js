// const ul = document.querySelector('.items')
// // console.log(ul)
// // ul.remove()
// ul.firstElementChild.textContent = 'Hello'
// ul.children[1].innerText = 'Forward'
// ul.lastElementChild.innerHTML = '<h1>Hello</h1>'

// const btn = document.querySelector('.btn')
// btn.style.background = 'purple'


const myForm = document. querySelector( '#my-form' ) ;
const nameInput = document.querySelector( '#name' ) ;
const emailInput = document.querySelector( '#email' );
const msg = document.querySelector('.msg' );
const userList = document.querySelector('#users');

myForm.addEventListener('submit',e => {
    e.preventDefault()

    if(nameInput.value === '' || emailInput.value ===''){
        msg.classList.add('error')
        msg.innerHTML = 'Please input your name and email!'
        setTimeout(()=>msg.remove(),3000)
    }else{
        const li = document.createElement('li')
        li.appendChild(document.createTextNode(`${nameInput.value}${emailInput.value}`))
        userList.append(li)
        
        nameInput.value = ''
        emailInput.value = ''
    }
})