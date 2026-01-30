











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
            li.innerText = `${event.author} pushed to ${event.to_branch}`
        }

        if (event.action === "pull_request") {
            li.innerText = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch}`;
        }

        get_ul.appendChild(li)
        last_event = event.created_at;

    })
}

fetchEvents();
setInterval(fetchEvents, 15000);