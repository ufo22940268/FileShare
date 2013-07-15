var dropHandler = function(e){
    var file,text;
    e.preventDefault();
    text = e.dataTransfer.getData && e.dataTransfer.getData('text/html');
    text = text.match(/src\=\"(http.*?)\"/i);
    text = text && text[1];
    file = e.dataTransfer.files && e.dataTransfer.files[0];
    console.log(file);
    console.log(text);
    upLoad(file, text);
}

//event
document.body.addEventListener('dragenter', function(e) {
　e.preventDefault();
}, false);

document.body.addEventListener('dragleave', function(e) {
　e.preventDefault();
}, false);

document.body.addEventListener('dragover', function(e) {
　e.preventDefault();
}, false);

document.body.addEventListener('drop', function(e) {
    dropHandler(e);
}, false);

var dragF= document.getElementById('drag-fileElement');	
$("#drag-fileElement").change(function() {
    var file = this.files[0];
    console.log("changed");
    console.log(file);
    console.log(file.name);
    upLoad(file);
});

var upLoadUrl = "/upload";
var upLoadFlag = true;
var dragT= document.getElementById('drag-text');	
var t1 = '拖拽图片到这里喵~';
var t2 = '图片上传中喵~';
var rs   = document.getElementById('rs');	
var rsT  = document.getElementById('rs-text');	

var upLoad = function(file, text){
    var xhr = new XMLHttpRequest();
    var url = upLoadUrl;
    var data;
    //check
    if(upLoadFlag === false){
        alert('正在上传文件');
        return false;
    }
    if(!file && !text){
        alert('文件不存在,请重试');
        return false;
    }

    if(text && !/^http/i.test(text)){
        alert('图片地址必须http打头');
        return false;
    }

    //upload
    data = new FormData();
    file && data.append('file', file);
    text && data.append('my_uploaded_url', text);
    xhr.open("POST", url);
    xhr.onreadystatechange = function(){
        var rsText;			
        if(xhr.readyState == 4 && xhr.status == 200){	
            upLoadFlag = true;		
            dragT.innerHTML = t1;	
            rsText = xhr.responseText;
            rs.style.display = 'block';
            rsT.value = rsText;				
        }
    }
    xhr.send(data);
    upLoadFlag = false;
    dragT.innerHTML = t2;
}
