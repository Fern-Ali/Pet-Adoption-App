// JavaScript source code

//let editArray = ["species", "notes", "age"]
//let miniform = `

//<form id=miniform>
//<div class="row text-center shadow text-shadow round p-2" style="color: deeppink; border: 3px solid rgba(243, 101, 219, 0.28); background-color: lightyellow">
//    <div class="col-4 round shadow" style="border: 3px solid rgba(243, 101, 219, 0.28); background-color: rgba(243, 101, 219, 0.28);">
//        <label class="pt-2 font-weight-bold"> Species </label/>

//    </div>

//    <div class="col-8">

//        <input class="form-control shadow round mt-1" id="name" name="name" required="" type="text" value="">
        
//    </div>

//</div>
//</form>


//`






//FEATURES FOR ICON BAR -- SIZE UP, CHANGE COLOR,  AND ADD ANIMATION ON HOVER//
$(".species-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
        /*$(this).addClass("pop_form");*/
        /*$("#pop_form").append(miniform);*/
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
        /*$("#miniform").remove();*/
    }
);





$(".notes-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
    }
);

$(".edit-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
    }
);

$(".bday-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
    }
);

$(".edit-icon").on("click", addPetPage);
$(".species-icon").on("click", editPetPage);

function addPetPage() {
    window.location.href = '/add';
    return false;
}

function editPetPage() {
    let id = $(this).attr('id');
    window.location.href = `/pets/${id}/edit`;
    return false;
}