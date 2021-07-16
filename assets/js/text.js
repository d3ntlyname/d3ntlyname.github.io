$(function () {
    var title = document.title
        , animSeq = ["/", "/", "\\", "|", "/"]
        , animIndex = 0
        , titleIndex = 0;

    function doInverseSpinZeroPitch() {
        var loadTitle = title.substring(0, titleIndex);
        if (titleIndex > title.length) {
            animIndex = 0;
            titleIndex = 0
        }
        if (animIndex > 3) {
            titleIndex++;
            animIndex = 0
        }
        document.title = loadTitle + animSeq[animIndex];
        animIndex++
    }
    window.setInterval(doInverseSpinZeroPitch, 150);
});
$(function () {
    $(".typed").typed({
        strings: ["python developer", "(nedo)coder", "c# beginner", "(type)hacker", "music lover...", "hmmm...", "yes, i\'m gay", "no, i\'m legend\*", "shell script¿", "bruh", 'i love the taste', 'of blood more', 'than meth', 'i absolutely give', 'a fuck what your', 'rh factor is', 'my love', 'languishes in', 'this short word', 'blood', 'your blood', 'streak is', 'essentially', 'your deadline'],
        typeSpeed: 35,
        backSpeed: 0,
        cursorChar: ['❚'],
        smartBackspace: true,
        fadeOut: true,
        loop: true,
    });
});
