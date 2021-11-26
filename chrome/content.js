let messageId;
let token;
let summary;

window.addEventListener("load", () => {

    // Find token
    chrome.storage.local.get(['key'], (result) => {
        if (!result.key) {
            authorize();
        }
    })

    // Add spinner during processing
    setSpinner();
    
    // Find all emails on the page
    emails = document.getElementsByClassName("zA");

    // Go through the list of emails and get their lastMessageId
    // Then fetch the tldr and insert it into the email element
    for (let i = 0; i < emails.length; i++) {
        let lastMessageId = emails[i].children[4].children[0].children[1].getAttribute('data-legacy-last-message-id');
        let summary = fetchBrief(lastMessageId);
        emails[i].setAttribute('title', 'TLDR: ' + summary.tldr + ' \nTime: ' + summary.time)
    }
 });

function authorize() {
  // TODO: authorization with google
}

function fetchBrief(msgId) {

    // fetch('http://localhost/tldr')
    // .then(response => response.json())
    // .then(data => {
    //   processing.setAttribute('hidden', '');
    //   return data
    // });
    //const resp = await fetch("http://localhost/tldr");
    //const tldr = await resp.json();

    return { tldr: "Sam must do this and Lev redo this", time: "8 hours"}
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