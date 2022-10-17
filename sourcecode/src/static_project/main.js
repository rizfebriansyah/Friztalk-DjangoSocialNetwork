$(document).ready(function(){
    console.log('hello there')
    $('#modal-btn').click(function(){
        console.log('working')
        $('.ui.rizmodal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
})