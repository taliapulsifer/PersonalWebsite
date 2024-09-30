//Function to set the background based on the weather

function setBackground(weather){
    let backgroundColor;

    switch(true){
        case weather.includes('rain'):
            backgroundColor = '#a4b0be'
            break;
        case weather.includes('cloud'):
            backgroundColor = '#dfe4ea'
            break;
        case weather.includes('clear'):
            backgroundColor = '#f1c40f'
            break;
        case weather.includes('snow'):
            backgroundColor = '#ffffff'
            break;
        default:
            backgroundColor = '#2f3640';
            break;
    }

    // Apply the background color to the body
    document.body.style.backgroundColor = backgroundColor;
}

setBackground(weatherDescription);