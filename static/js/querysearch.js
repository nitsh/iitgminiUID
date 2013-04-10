var counter = 1;
var inputCounter = 0;
var counterText = 0;
var counterRadioButton = 0;
var counterCheckBox = 0;
var counterTextArea = 0;
function addAllInputs(divName, inputType){
    var newdiv = document.createElement('div');
    switch(inputType) {
        case 'text':
            newdiv.innerHTML = " Add More " + (counterText + 1) + " <br><input type='text' name='myInputs[]'>";
            counterText++;
            break;
        case 'radio':
            newdiv.innerHTML = "Entry " + (counterRadioButton + 1) + " <br><input type='radio' >";
            counterRadioButton++;
            break;
        case 'checkbox':
            newdiv.innerHTML = "Add Filter <br><input type='checkbox' onchange='createNewOption()'>";
            counterCheckBox++;
            break;
        case 'textarea':
            newdiv.innerHTML = "Entry " + (counterTextArea + 1) + " <br><textarea name='myTextAreas[]'>type here...</textarea>";
            counterTextArea++;
            break;
    }
    document.getElementById(divName).appendChild(newdiv);
}

function createNewElement(id)
{
    var ID = "input" + inputCounter;
    //if (counter == limit){
    //alert("You have reached the limit of adding " + counter + " inputs");
    //}
    //else {
    //if(id === inputCounter-1 )
    //{
        //id = "where" + id;
    //}
    //var callerID = "where" + (inputCounter);
    //alert("II"+inputCounter);
    //alert("calling id" + id);
    //var x=document.getElementById( callerID );
    //if(callerID !== id)
    //{
    //    alert("already present" + callerID);
    //}
    //else
    //{
    inputCounter++;
    var newdiv = document.createElement("input");
    newdiv.setAttribute("name", ID);
    newdiv.setAttribute("id", ID);
    newdiv.setAttribute("type", "text");
    newdiv.style.width = "300px";
    //newdiv.innerHTML = "is " + " <br><input type='text' id=" + ID + " name=" + ID + ">";
    //newdiv.innerHTML = "";
    document.queryform.appendChild(newdiv);
    addAllInputs( 'form1', 'checkbox' );
    //}
}

function createNewOption()
{
    var ID = "where" + counter;
    counter++;
    var select = document.createElement("select");
    select.setAttribute("name", ID);
    select.setAttribute("id", ID);
    //alert("GGG"+ID);
    //select.style.width = "300px";
    /* setting an onchange event */
    select.onchange = function() {createNewElement(2)};
    var option;

    var fields= new Array();
    var x=document.getElementById("where0");
    for (var i=0;i<x.length;i++)
    { 
        fields[i]=x.options[i].text;
        //alert(fields[i]);
    
        /* we are going to add two options */
        /* create options elements */
        option = document.createElement("option");
        option.setAttribute("value", fields[i] );
        option.innerHTML = fields[i];
        select.appendChild(option);
    }
    document.queryform.appendChild(select);
}

//
//function searchquery( formElement )
//{
//    alert("IN SEARCH SUBMIT");
//    var inputs, selects, index;
//    inputs = document.getElementsByTagName('input');
//    selects = document.getElementsByTagName('select');
//    for (index = 0; index < inputs.length; ++index)
//    {
//        // deal with inputs[index] element.
//        var name = inputs[index];
//        alert( name );
//    }
//
//    return true;
//}
