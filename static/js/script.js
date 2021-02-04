/**
 * Materialize jQuery
 * @external Materialize
 * @see {@link https://materializecss.com/}
 * @external jQuery
 * @see {@link http://api.jquery.com/jQuery/}
 */

$(document).ready(function () {

    //Button collapse for mobile navigation menu.
    $(".button-collapse").sideNav({
        menuWidth: 200,
        edge: 'right'
    });

    // Within mobile sidenav, dropdown menu appears when clicked.
    $('.dropdown-trigger').dropdown();

    // For Desktop navigation, dropdown menu appears when hovered.
    $('.dropdown-button').dropdown({
        inDuration: 400,
        outDuration: 225,
        hover: true
    });

    // Image carousel will scroll periodically dictated by setInterval function. Touch compatible.
    $('.carousel').carousel();
    setInterval(function () {
        $('.carousel').carousel('next');
    }, 3000);

    // Material box centers the image and enlarges it by clicking.
    $('.materialboxed').materialbox();

    //Tooltip will appear when user hovers mouse over certain elements.
    $('.tooltipped').tooltip({ delay: 50 });

    // Modal message appears when user clicks certain buttons. Eg, Delete Recipe button.
    $('.modal').modal();

    // Copyright date will be automatically updated every year without user input.
    $("#copyright").text(new Date().getFullYear());

    // User is able to click on option and is able to choose from additional options.
    $('select').material_select();

    // When 'To Top Button' is clicked: Scroll to top of page in 800ms.
    $("a[href='#top']").click(function () {
        $("html, body").animate({ scrollTop: 0 }, 800);
        return false;
    });

    // If position of vertical scroll is above 200px, to top button will disappear.
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.to-top').fadeIn();
        } else {
            $('.to-top').fadeOut();
        }
    });

    // Changes and applies class styles depending on how user interacts with form fields.
    // Sets select element to be physically on DOM, and applies different classes when needed.
    validateMaterializeSelect();
    function validateMaterializeSelect() {

        // Set CSS colors for validation - Red or green.
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };

        // Set select element to be physically on the DOM.
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }

        // Apply green valid class when clicked.
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });

        // Apply a green valid class again, if there isn't either the valid or invalid classes, based on the same DOM traversing above.
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {

                // Apply invalid red class if user comes out of selection, and bottom-border wasn't updated.
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