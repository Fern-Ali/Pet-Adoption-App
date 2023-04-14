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

let home = 'https://github.com/Fern-Ali/';
let repo = 'https://github.com/Fern-Ali/Pet-Adoption-App';
let reqs = 'https://github.com/Fern-Ali/Pet-Adoption-App/blob/master/requirements.txt';


document.body.style.background = "url('https://images.unsplash.com/photo-1529472119196-cb724127a98e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=672&q=80')  ";

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

$(".github-icon").hover(
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

$(".reqs-icon").hover(
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
$(".github-icon").on("click", {event_type: home}, goToGithub);
$(".project-icon").on("click", {event_type: repo}, goToGithub);
$(".reqs-icon").on("click", {event_type: reqs}, goToGithub);



function addPetPage() {
    window.location.href = '/add';
    return false;
}

function editPetPage() {
    let id = $(this).attr('id');
    window.location.href = `/pets/${id}/edit`;
    return false;
}

function goToGithub( event ) {
    
    window.location.href = event.data.event_type;
    return false;
}