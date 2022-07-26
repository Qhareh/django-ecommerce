$('#myTab a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
})

var updatebtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updatebtns.length; i++){
    updatebtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', username)
        if(username === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            console.log('User is logged in, sending data..')
        }
    })
}