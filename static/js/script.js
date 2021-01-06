$(document).ready(function () {
    // Side nav for mobile view
    $(".button-collapse").sideNav({
        edge: 'right'
    });

    // Clickable recipes dropdown menu for mobile side-nav
    $('.dropdown-trigger').dropdown();

    // Hoverable recipes dropdown menu for desktop
    $('.dropdown-button').dropdown({
        inDuration: 400,
        outDuration: 225,
        hover: true
    });

    // Image animation that scrolls through different images
    $('.carousel').carousel();
    setInterval(function () {
        $('.carousel').carousel('next');
    }, 3000);

    // Clickable images to make full screen with message
    $('.materialboxed').materialbox();

    // Tooltip messages for Success Stories
    $('.tooltipped').tooltip({ delay: 50 });

    // Modal to appear when success story images are clicked
    $('.modal').modal();

    // Copyright date updated every year
    $("#copyright").text(new Date().getFullYear());

    // Select dropdown box for Add Recipe form
    $('select').material_select();

    // Materialize form validation for select dropdown
    validateMaterializeSelect();
    function validateMaterializeSelect() {

        // Set CSS colors for validation - red or green
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };

        // Set select element to be physically on the DOM
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }

        // Apply green valid class when clicked
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });

        // Apply a green valid class again, if there isn't either the valid or invalid classes, based on the same DOM traversing above
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {

                // Apply invalid red class if user comes out of selection, and bottom-border wassn't updated
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});