$(function () {
    var title = document.title
        , animSeq = ["/", "$", "\\", "|", "$"]
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
        strings: ["Kto eto?", "Python developer", "Nedocoder", "C# beginner", "Typehacker", "Music lover...", "Hmmm", "Bruh"],
        typeSpeed: 50,
        loop: true,
        cursorChar: ["/", "$", "\\", "|", "$"],
    });
});
