function formatTimestamp(isoString) {
    const date = new Date(isoString);

    const day = date.getUTCDate();
    const suffix =
        (day >= 11 && day <= 13) ? "th" :
            (day % 10 === 1) ? "st" :
                (day % 10 === 2) ? "nd" :
                    (day % 10 === 3) ? "rd" : "th";

    const dayWithSuffix = `${day}${suffix}`;

    const month = date.toLocaleString("en-US", {
        month: "long",
        timeZone: "UTC"
    });

    const year = date.getUTCFullYear();

    const time = date.toLocaleString("en-US", {
        hour: "numeric",
        minute: "2-digit",
        hour12: true,
        timeZone: "UTC"
    });

    return `${dayWithSuffix} ${month} ${year} - ${time} UTC`;
}










let last_event = null;

async function fetchEvents() {

    let url = ''

    if (last_event === null) {
        url = 'http://127.0.0.1:5000/webhook/events'
    } else {

        url = `http://127.0.0.1:5000/webhook/events?after=${encodeURIComponent(last_event)}`
    }

    const res = await fetch(url)
    const data = await res.json()


    const get_ul = document.getElementById('events_list')

    data.events.forEach(event => {
        const li = document.createElement('li')

        if (event.action === 'push') {
            li.innerText = `${event.author} pushed to ${event.to_branch} on ${formatTimestamp(event.timestamp)}`
        }

        if (event.action === "pull_request") {
            li.innerText = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${formatTimestamp(event.timestamp)} `
        }

        get_ul.appendChild(li)
        last_event = event.created_at;

    })
}

fetchEvents();
setInterval(fetchEvents, 15000);