let messageId;
let token;
let summary;

window.addEventListener("load", async () => {

    // Add spinner during processing
    setSpinner();
    
    // Find all emails on the page
    emails = document.getElementsByClassName("zA");

    // Go through the list of emails and get their lastMessageId
    // Then fetch the tldr and insert it into the email element
    for (let i = 0; i < emails.length; i++) {
        let lastMessageId = emails[i].children[4].children[0].children[1].getAttribute('data-legacy-last-message-id');
        let summary = await fetchBrief(lastMessageId);
        emails[i].setAttribute('title', 'TLDR: ' + summary.tldr + ' \nTime: ' + summary.time)
    }
    processing.setAttribute('hidden', '');
 });


async function fetchBrief(msgId) {
    const resp = await fetch('http://localhost:5000/task_by_email?id='+ msgId);
    return await resp.json();
}

function setSpinner() {
    let processing = document.createElement('div')
    processing.setAttribute('id', 'processing');

    let spinner = document.createElement('div');
    spinner.setAttribute('id', 'spinner');
    processing.appendChild(spinner)

    let message = document.createElement('p');
    message.setAttribute('id', 'message');
    message.innerText = "Processing TLDRs";

    processing.appendChild(message)
   
    let attachTo = document.getElementById(":4");
    attachTo.appendChild(processing);
}