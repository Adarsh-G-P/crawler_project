

import logo from './logo.svg';
import './App.css';

//usestate =define the state variables artist, track, lyrics will hold the data fetched from the backend
//useeffect thelist of artists from backend 
import { useState, useRef, useEffect } from 'react';

import axios, * as others from 'axios';


//App component interacts with the backend API by making HTTP requests to fetch
// artists, tracks, and lyrics based on user interactions. 
//The fetched data is then displayed in the user interface using JSX and CSS styles.



function App() {
    const [artists, setArtists] = useState([]);
    const [tracks, setTracks] = useState([])
    const [lyrics, setLyrics] = useState([])


    useEffect(() => {
        axios.get("http://127.0.0.1:8000//api/v1/artist")
            .then((resp) => {
                setArtists(resp.data.artists);
                setTracks([])
                setLyrics([])
            });
    }, []);
//This function is triggered when an artist link is clicked.
// makes an HTTP GET request to the /api/v1/artist/{artistId} endpoint 
//to fetch the tracks of the selected artist
//The fetched tracks are set in the tracks state

    function onClickHandlerTracks(e) {
        e.preventDefault();
        const artistId = e.currentTarget.getAttribute('artist_id');
        axios.get(`http://127.0.0.1:8000/api/v1/artist/${artistId}`)
            .then((resp) => {
                setTracks(resp.data.tracks);
                setLyrics([])
            });
    }

//fetch the lyrics of the selected track. 
//The fetched lyrics are set in the lyrics state.

    function onClickHandlerLyrics(e) {
        e.preventDefault()
        const trackId = e.currentTarget.getAttribute('track_id')
        // console.log(trackId)
        axios.get(`http://127.0.0.1:8000/api/v1/song/${trackId}`)
            .then((resp) => {
                setLyrics([resp.data])
                console.log(resp.data)
            })
    }


        //The fetched artists are rendered as an ordered list (<ol>) 
        //with each artist name as a list item (<li>). 
        //Each artist name is a link that triggers the onClickHandlerTracks function when clicked.

        //The fetched tracks are rendered as an unordered list (<ul>) 
        //with each track name as a list item (<li>). 
        //Each track name is a link that triggers the onClickHandlerLyrics function when clicked.
    return (
        <div className="row">
            <div className="col">
                <h2> Artists </h2>
                <ol>
                    {artists.map(((artist, idx) => <li key={`artist${artist.id}`}>
                        <a
                            href={`http://127.0.0.1:8000/api/v1/artist/${artist.id}`}
                            onClick={onClickHandlerTracks}
                            artist_id={artist.id}
                        >{artist.name}
                        </a>
                    </li>))}
                </ol>
            </div>
            

            <div className="col">
                <h2> Tracks </h2>
                <ul>
                    {tracks.map(((track, idx) => <li key={`track${track.id}`}>
                        <a
                            href={`http://127.0.0.1:8000/api/v1/song/${track.id}`}
                            onClick={onClickHandlerLyrics}
                            track_id={track.id}
                        >{track.name}
                        </a>
                    </li>))}
                </ul>
            </div>


            <div className="col">
                <h2> Lyrics </h2>
                {lyrics.map(((lyric, idx) => 
                <div key={idx}>
                    <div>{lyric.name}</div>
                    <div style={{ whiteSpace: 'pre-line' }}>{lyric.lyrics}</div>
                </div>))}

            </div>
        </div>
    );
}
//The fetched lyrics are rendered as a <div> for each lyric item.
// The name of the track is displayed as a separate <div>, and the lyrics are displayed
// as text within a <div> with the whiteSpace CSS property set to 'pre-line' to preserve line breaks.
export default App;

