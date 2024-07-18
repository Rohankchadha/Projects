var loadfile = function(event){
    var output=document.getElementById("output")
    var target=document.getElementById("target")
    for(let i = 0; i<10; i++){
        output.innerHTML+= ('<img class="class'+i+'" src="'+URL.createObjectURL(event.target.files[i])+'" width="100px" height="100px" alt="select image to preview">')
        target.innerHTML+= ('<button type="button" id="class'+i+'" width="100px" #onclick="delt(this.id)">Delete</button>')
    }
}
// var delt = function(id){
//     var target1=document.getElementsByClassName(id)
//     alert(target1.id)
    
// }