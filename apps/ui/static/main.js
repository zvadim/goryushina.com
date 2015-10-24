$(document).ready(function(){
    $('#carousel-page-gallery').slick({
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        swipe: false,
        variableWidth: true
    });

    $(".fancybox").fancybox({
        padding: 0
    });
});