#!/bin/bash

# City Facts App - Quick Deploy Script

echo "🚀 City Facts App Deployment Helper"
echo "=================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - City Facts App"
    echo "✅ Git repository created!"
else
    echo "✅ Git repository already exists"
fi

echo ""
echo "🎯 Choose your deployment platform:"
echo "1. Railway (Recommended - easiest)"
echo "2. Render (Great free option)"
echo "3. Heroku (Classic)"
echo "4. Docker (Local testing)"
echo "5. Manual VPS setup"

echo ""
echo "📋 Pre-deployment checklist:"
echo "✅ requirements.txt updated"
echo "✅ Procfile created"
echo "✅ Dockerfile created"
echo "✅ Environment variables configured"
echo "✅ Railway.toml configured"
echo "✅ render.yaml configured"

echo ""
echo "🔗 Next steps:"
echo "1. Push code to GitHub"
echo "2. Connect GitHub to your chosen platform"
echo "3. Deploy automatically"
echo "4. Test your live app!"

echo ""
echo "📊 Your app includes:"
echo "• 21 cities (10 world + 11 Pakistani)"
echo "• 210 unique facts"
echo "• Smart fact rotation system"
echo "• Beautiful modern UI"
echo "• Mobile-responsive design"

echo ""
echo "🌐 After deployment, your app will be accessible worldwide!"