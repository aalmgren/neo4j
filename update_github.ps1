# Script para atualizar o GitHub Pages com force push
# Execute: .\update_github.ps1

Write-Host "Inicializando Git..." -ForegroundColor Yellow
git init

Write-Host "Configurando remote..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin https://github.com/aalmgren/neo4j.git

Write-Host "Adicionando todos os arquivos..." -ForegroundColor Yellow
git add -A

Write-Host "Fazendo commit..." -ForegroundColor Yellow
git commit -m "Update: Improved layout, word wrap, legend positioning, fading logic, and added index page with tabs"

Write-Host "Configurando branch main..." -ForegroundColor Yellow
git branch -M main

Write-Host "Fazendo push forçado para sobrescrever arquivos antigos..." -ForegroundColor Yellow
git push -f origin main

Write-Host "`n✅ Concluído! O GitHub Pages será atualizado em 1-2 minutos." -ForegroundColor Green
Write-Host "Acesse: https://aalmgren.github.io/neo4j/index.html" -ForegroundColor Cyan

