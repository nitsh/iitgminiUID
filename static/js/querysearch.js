var whereCounter = 1;
var inputCounter = 0;
var counter = 0;
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
            newdiv.innerHTML = "Add Filter <br><input type='checkbox'>";
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
    var inputRequired = true;
    //document.getElementById(id).disabled=true;
    var ID = "input" + counter;
    var inputType = "text"
    var currWhereID = "where" + counter;
    var attribute = document.getElementById( currWhereID );
    if ( attribute){
        var attributeType = attribute.options[attribute.selectedIndex].text;
        // give special treatement to some attributes
        if ( attributeType.search( 'age' ) != -1 ){
            var comparatorID = "comparator" + counter;
            var options = new Array("==","<",">");
            createDropdown( comparatorID, options, "80px" );
        }
        if ( attributeType.search( 'gender' ) != -1 ){
            inputRequired = false;
            var comparatorID = "input" + counter;
            var options = new Array("male","female");
            createDropdown( comparatorID, options, "300px" );
        }
        if ( attributeType.search( 'type' ) != -1 ){
            inputRequired = false;
            var comparatorID = "input" + counter;
            var options = new Array("student","faculty","staff","others");
            createDropdown( comparatorID, options, "300px" );
        }
        if ( attributeType.search( 'bloodGroup' ) != -1 ){
            inputRequired = false;
            var comparatorID = "input" + counter;
            var options = new Array("AB+","AB-","O-","O+","A+","A-","B+","B-","Bombay");
            createDropdown( comparatorID, options, "300px" );
        }
        if ( attributeType.search( 'hostel' ) != -1 ){
            inputRequired = false;
            var comparatorID = "input" + counter;
            var options = new Array("Barak","Brahmaputra","Dibang","Dihing","Kameng","Kapili","Manas","Siang","Subansiri","Umiam");
            createDropdown( comparatorID, options, "300px" );
        }
        if ( attributeType.search( 'post' ) != -1 ){
            inputRequired = false;
            var comparatorID = "input" + counter;
            var options = new Array("assistant Professor","Associate","Professor");
            createDropdown( comparatorID, options, "300px" );
        }
        if ( attributeType.search( 'dob' ) != -1 ){
            inputType = "date";
        }

    }
    if(id != currWhereID){
        // code to change input type needs to be WRITTEN here
        //alert( id + "    yes::" + currWhereID);

    }
    else if (inputRequired){
        inputRequired = false;
        var newdiv = document.createElement("input");
        newdiv.setAttribute("name", ID);
        newdiv.setAttribute("id", ID);
        newdiv.setAttribute("type", inputType);
        newdiv.style.width = "300px";
        //newdiv.innerHTML = "is " + " <br><input type='text' id=" + ID + " name=" + ID + ">";
        document.queryform.appendChild(newdiv);
    }
    if( !inputRequired){
        // create button for and/or
        var addFilterID = "addifilter"+counter;
        var option = new Array('','AND','OR');
        createDropdown( addFilterID, option, "100px");
        document.getElementById(addFilterID).onchange = function(){createNewOption()};
        br = document.createElement("br");
        document.queryform.appendChild( br );
        //createNewOption();
        var node=document.createTextNode(" ");
        document.queryform.appendChild(node);
    }
}

function createNewOption()
{
    counter++;
    var ID = "where" + counter;
    var curraddFilterID = "addfilter" + (counter-1);
    var attribute = document.getElementById( curraddFilterID );
    if ( attribute){
        alert(curraddFilterID);
    }
    else{
        var fields= new Array();
        var x=document.getElementById("where0");
        for (var i=0;i<x.length;i++){ 
            fields[i]=x.options[i].text;
        }
        createDropdown(ID, fields, "220px");
        document.getElementById(ID).onchange = function(){createNewElement(ID)};
    }
}


function createDropdown( id , fields, width)
{
    var ID = id;
    var select = document.createElement("select");
    select.setAttribute("name", ID);
    select.setAttribute("id", ID);
    select.style.width = width;
    var option;
    for (var i=0;i<fields.length;i++)
    {
        option = document.createElement("option");
        option.setAttribute("value", fields[i] );
        option.innerHTML = fields[i];
        select.appendChild(option);
    }
    document.queryform.appendChild(select);
}
