
const button = document.querySelector('.form_button')
const inputs = document.querySelectorAll('.input__form')

const message = "Администратор проверит новость и, если она пройдет проверку, опубликует её." ;

button.addEventListener('click' , () => {

    let allow = true
    inputs.forEach( item => { if (item.value == '') allow = false } )

    if (allow) alert(message)
})