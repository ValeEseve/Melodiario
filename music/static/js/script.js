document.getElementById('album-search').addEventListener('input', async function() {
    const query = this.value.trim();
    const resultsContainer = document.getElementById('search-results');
    resultsContainer.innerHTML = '';

    if (query.length < 3) return;

    const response = await fetch(`https://musicbrainz.org/ws/2/release/?query=release:${encodeURIComponent(query)}&fmt=json`);
    const data = await response.json();

    data.releases.slice(0,5).forEach(release => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'list-group-item-action');
        li.textContent = `${release.title} – ${release['artist-credit'].map(a => a.name).join(', ')}`;
        li.addEventListener('click', async () => {
            // Rellenar campos del form
            document.getElementById('id_title').value = release.title;
            document.getElementById('id_musicbrainz_id').value = release.id;
            
            // Opcional: fecha de lanzamiento
            if (release.date) {
                document.getElementById('id_release_date').value = release.date;
            }

            // Portada
            try {
                const coverUrl = `https://coverartarchive.org/release/${release.id}/front-250`;
                const img = document.createElement('img');
                img.src = coverUrl;
                img.classList.add('img-fluid', 'mt-2');
                if (!document.getElementById('cover-preview')) {
                    img.id = 'cover-preview';
                    resultsContainer.appendChild(img);
                } else {
                    document.getElementById('cover-preview').src = coverUrl;
                }
            } catch(e) { console.log('No cover art available'); }

            resultsContainer.innerHTML = '';
        });
        resultsContainer.appendChild(li);
    });
});

document.getElementById('song-search').addEventListener('input', async function() {
    const query = this.value.trim();
    const resultsContainer = document.getElementById('song-results');
    resultsContainer.innerHTML = '';

    if (query.length < 3) return;

    const response = await fetch(`https://musicbrainz.org/ws/2/recording/?query=recording:${encodeURIComponent(query)}&fmt=json`);
    const data = await response.json();

    data.recordings.slice(0,5).forEach(recording => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'list-group-item-action');
        li.textContent = `${recording.title} – ${recording['artist-credit'].map(a => a.name).join(', ')}`;
        
        li.addEventListener('click', async () => {
            // Rellenar campos del form
            document.getElementById('id_title').value = recording.title;
            document.getElementById('id_musicbrainz_id').value = recording.id;

            // Seleccionar álbum si existe
            if (recording.releases && recording.releases.length > 0) {
                const albumSelect = document.getElementById('id_album');
                const release = recording.releases[0];
                for (let i=0; i<albumSelect.options.length; i++) {
                    if (albumSelect.options[i].text.includes(release.title)) {
                        albumSelect.selectedIndex = i;
                        break;
                    }
                }

                // Portada del álbum
                try {
                    const coverUrl = `https://coverartarchive.org/release/${release.id}/front-250`;
                    const img = document.createElement('img');
                    img.src = coverUrl;
                    img.classList.add('img-fluid', 'mt-2');
                    if (!document.getElementById('cover-preview')) {
                        img.id = 'cover-preview';
                        resultsContainer.appendChild(img);
                    } else {
                        document.getElementById('cover-preview').src = coverUrl;
                    }
                } catch(e) { console.log('No cover art available'); }
            }

            resultsContainer.innerHTML = '';
        });

        resultsContainer.appendChild(li);
    });
});