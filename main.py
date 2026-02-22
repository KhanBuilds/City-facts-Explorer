from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random
import os
from typing import Dict, List
from cities_data import CITIES_FACTS

# Track shown facts for each city to avoid immediate repeats
city_fact_tracker = {}

app = FastAPI(title="City Facts API", description="Get random facts about cities around the world")

@app.get("/")
async def home():
    """Home page with city selection interface"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>City Facts Explorer</title>
        <style>
            * {
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            
            .container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                animation: slideUp 0.6s ease-out;
            }
            
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            h1 {
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-align: center;
                margin-bottom: 10px;
                font-size: 2.5rem;
                font-weight: 700;
                text-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 40px;
                font-size: 1.1rem;
                opacity: 0;
                animation: fadeIn 0.8s ease-out 0.3s forwards;
            }
            
            @keyframes fadeIn {
                to {
                    opacity: 1;
                }
            }
            
            select {
                width: 100%;
                padding: 16px 20px;
                font-size: 16px;
                border: 2px solid #e0e0e0;
                border-radius: 12px;
                margin-bottom: 25px;
                background: white;
                transition: all 0.3s ease;
                cursor: pointer;
            }
            
            select:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
                transform: translateY(-2px);
            }
            
            select:hover {
                border-color: #667eea;
            }
            
            button {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                padding: 16px 24px;
                font-size: 18px;
                font-weight: 600;
                border: none;
                border-radius: 12px;
                cursor: pointer;
                width: 100%;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            
            button:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
            }
            
            button:active {
                transform: translateY(-1px);
            }
            
            button:disabled {
                background: #ccc;
                cursor: not-allowed;
                transform: none;
            }
            
            .fact-box {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                padding: 25px;
                margin-top: 30px;
                border-radius: 15px;
                display: none;
                opacity: 0;
                box-shadow: 0 15px 35px rgba(240, 147, 251, 0.3);
                position: relative;
                overflow: hidden;
            }
            
            .fact-box::before {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(45deg, #f093fb, #f5576c, #4facfe, #00f2fe);
                border-radius: 15px;
                z-index: -1;
                animation: borderGlow 3s ease-in-out infinite;
            }
            
            @keyframes borderGlow {
                0%, 100% { transform: rotate(0deg); }
                50% { transform: rotate(180deg); }
            }
            
            .fact-box.show {
                display: block;
                animation: factSlide 0.6s ease-out forwards;
            }
            
            @keyframes factSlide {
                from {
                    opacity: 0;
                    transform: translateX(-30px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            
            .fact-city {
                font-size: 1.4rem;
                font-weight: 700;
                margin-bottom: 15px;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            }
            
            .fact-text {
                font-size: 1.1rem;
                line-height: 1.6;
                margin-bottom: 15px;
                text-shadow: 0 1px 2px rgba(0,0,0,0.2);
            }
            
            .fact-counter {
                font-size: 0.9rem;
                opacity: 0.9;
                font-weight: 500;
            }
            
            .city-group {
                font-weight: bold;
                color: #667eea;
                font-size: 0.95rem;
            }
            
            .loading {
                display: none;
                text-align: center;
                margin-top: 20px;
            }
            
            .spinner {
                border: 3px solid #f3f3f3;
                border-top: 3px solid #667eea;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 0 auto;
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌍 City Facts Explorer</h1>
            <p class="subtitle">Discover fascinating facts about cities from around the world and Pakistan!</p>
            
            <select id="citySelect">
                <option value="">Select a city...</option>
                <optgroup label="🌍 World Cities" class="city-group">
                    <option value="Tokyo">Tokyo, Japan</option>
                    <option value="New York">New York, USA</option>
                    <option value="London">London, UK</option>
                    <option value="Paris">Paris, France</option>
                    <option value="Rome">Rome, Italy</option>
                    <option value="Sydney">Sydney, Australia</option>
                    <option value="Dubai">Dubai, UAE</option>
                    <option value="Singapore">Singapore</option>
                    <option value="Moscow">Moscow, Russia</option>
                    <option value="Cairo">Cairo, Egypt</option>
                </optgroup>
                <optgroup label="🇵🇰 Pakistan Cities" class="city-group">
                    <option value="Karachi">Karachi</option>
                    <option value="Lahore">Lahore</option>
                    <option value="Islamabad">Islamabad</option>
                    <option value="Rawalpindi">Rawalpindi</option>
                    <option value="Faisalabad">Faisalabad</option>
                    <option value="Multan">Multan</option>
                    <option value="Peshawar">Peshawar</option>
                    <option value="Quetta">Quetta</option>
                    <option value="Sialkot">Sialkot</option>
                    <option value="Gujranwala">Gujranwala</option>
                    <option value="Sargodha">Sargodha</option>
                </optgroup>
            </select>
            
            <button id="factButton" onclick="getRandomFact()">Get Random Fact! 🎲</button>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Discovering amazing facts...</p>
            </div>
            
            <div id="factBox" class="fact-box">
                <h3 class="fact-city" id="factCity"></h3>
                <p class="fact-text" id="factText"></p>
                <p class="fact-counter" id="factCounter"></p>
            </div>
        </div>

        <script>
            let cityFactState = {}; // Track shown facts per city
            
            async function getRandomFact() {
                const citySelect = document.getElementById('citySelect');
                const factButton = document.getElementById('factButton');
                const loading = document.getElementById('loading');
                const factBox = document.getElementById('factBox');
                const selectedCity = citySelect.value;
                
                if (!selectedCity) {
                    showNotification('Please select a city first! 🏙️', 'warning');
                    return;
                }
                
                // Show loading state
                factButton.disabled = true;
                factButton.textContent = 'Getting Fact...';
                loading.style.display = 'block';
                factBox.classList.remove('show');
                
                try {
                    const response = await fetch(`/city/${selectedCity}/fact`);
                    const data = await response.json();
                    
                    if (response.ok) {
                        // Simulate loading delay for better UX
                        setTimeout(() => {
                            // Initialize city state if not exists
                            if (!cityFactState[selectedCity]) {
                                cityFactState[selectedCity] = {
                                    shownFacts: new Set(),
                                    currentCycle: 1
                                };
                            }
                            
                            const state = cityFactState[selectedCity];
                            state.shownFacts.add(data.fact);
                            
                            // Check if we've seen all facts for this city
                            if (state.shownFacts.size >= data.total_facts) {
                                state.currentCycle++;
                                state.shownFacts.clear();
                                state.shownFacts.add(data.fact);
                            }
                            
                            document.getElementById('factCity').textContent = `${data.city} ✨`;
                            document.getElementById('factText').textContent = data.fact;
                            document.getElementById('factCounter').textContent = 
                                `Fact ${state.shownFacts.size}/${data.total_facts} • Cycle ${state.currentCycle}`;
                            
                            loading.style.display = 'none';
                            factBox.classList.add('show');
                            factButton.disabled = false;
                            factButton.textContent = 'Get Random Fact! 🎲';
                            
                            // Show completion message when cycle completes
                            if (state.shownFacts.size === 1 && state.currentCycle > 1) {
                                setTimeout(() => {
                                    showNotification(`🎉 You've discovered all ${data.total_facts} facts about ${data.city}! Starting new cycle.`, 'success');
                                }, 1000);
                            }
                        }, 800);
                    } else {
                        loading.style.display = 'none';
                        factButton.disabled = false;
                        factButton.textContent = 'Get Random Fact! 🎲';
                        showNotification('Error: ' + data.detail, 'error');
                    }
                } catch (error) {
                    loading.style.display = 'none';
                    factButton.disabled = false;
                    factButton.textContent = 'Get Random Fact! 🎲';
                    showNotification('Error fetching fact: ' + error.message, 'error');
                }
            }
            
            function showNotification(message, type) {
                // Create notification element
                const notification = document.createElement('div');
                notification.style.cssText = `
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    padding: 15px 25px;
                    border-radius: 10px;
                    color: white;
                    font-weight: 600;
                    z-index: 1000;
                    animation: slideIn 0.3s ease-out;
                    max-width: 400px;
                    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                `;
                
                // Set background based on type
                switch(type) {
                    case 'success':
                        notification.style.background = 'linear-gradient(45deg, #4CAF50, #45a049)';
                        break;
                    case 'warning':
                        notification.style.background = 'linear-gradient(45deg, #FF9800, #F57C00)';
                        break;
                    case 'error':
                        notification.style.background = 'linear-gradient(45deg, #f44336, #d32f2f)';
                        break;
                }
                
                notification.textContent = message;
                document.body.appendChild(notification);
                
                // Add animation keyframe
                if (!document.getElementById('notificationStyle')) {
                    const style = document.createElement('style');
                    style.id = 'notificationStyle';
                    style.textContent = `
                        @keyframes slideIn {
                            from { transform: translateX(100%); opacity: 0; }
                            to { transform: translateX(0); opacity: 1; }
                        }
                    `;
                    document.head.appendChild(style);
                }
                
                // Remove notification after 4 seconds
                setTimeout(() => {
                    notification.style.animation = 'slideIn 0.3s ease-out reverse';
                    setTimeout(() => {
                        if (notification.parentNode) {
                            notification.parentNode.removeChild(notification);
                        }
                    }, 300);
                }, 4000);
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/cities")
async def get_cities() -> List[str]:
    """Get list of available cities"""
    return list(CITIES_FACTS.keys())

@app.get("/city/{city_name}/fact")
async def get_city_fact(city_name: str):
    """Get a smart random fact about a specific city (avoids immediate repeats)"""
    # Normalize city name (case-insensitive lookup)
    city_key = None
    for key in CITIES_FACTS.keys():
        if key.lower() == city_name.lower():
            city_key = key
            break
    
    if not city_key:
        raise HTTPException(status_code=404, detail=f"City '{city_name}' not found")
    
    facts = CITIES_FACTS[city_key]
    
    # Initialize tracker for this city if not exists
    if city_key not in city_fact_tracker:
        city_fact_tracker[city_key] = {
            "used_facts": set(),
            "available_facts": set(facts)
        }
    
    tracker = city_fact_tracker[city_key]
    
    # If all facts have been used, reset the cycle
    if not tracker["available_facts"]:
        tracker["available_facts"] = set(facts)
        tracker["used_facts"] = set()
    
    # Select a random fact from available facts
    selected_fact = random.choice(list(tracker["available_facts"]))
    
    # Update tracker
    tracker["used_facts"].add(selected_fact)
    tracker["available_facts"].remove(selected_fact)
    
    return {
        "city": city_key,
        "fact": selected_fact,
        "total_facts": len(facts),
        "facts_shown": len(tracker["used_facts"]),
        "cycle_complete": len(tracker["available_facts"]) == 0
    }

@app.get("/city/{city_name}/facts")
async def get_all_city_facts(city_name: str):
    """Get all facts about a specific city"""
    # Normalize city name (case-insensitive lookup)
    city_key = None
    for key in CITIES_FACTS.keys():
        if key.lower() == city_name.lower():
            city_key = key
            break
    
    if not city_key:
        raise HTTPException(status_code=404, detail=f"City '{city_name}' not found")
    
    return {
        "city": city_key,
        "facts": CITIES_FACTS[city_key],
        "total_facts": len(CITIES_FACTS[city_key])
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)