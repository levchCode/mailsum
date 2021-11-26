window.addEventListener("load", function() {
    emails = document.getElementsByClassName("zA");
    console.log(emails[0])

    for (let i = 0; i < emails.length; i++) {
        let text = getText(emails[i]);
        let tldr = fetchBrief(text);
        insertBrief(emails[i], tldr);
    }
 });

function fetchBrief(text) {
    //const resp = await fetch("http://localhost/tldr");
    //const tldr = await resp.json();

    return { tldr: "Sam must do this and Lev redo this", time: "8 hours"}
}

function insertBrief(mailElement, summary) {
    mailElement.setAttribute('title', 'TLDR: ' + summary.tldr + ' \nTime: ' + summary.time)
}

function getText(mailElement) {
    // TODO processing
    return "Dear Lev, do this, do that"
}