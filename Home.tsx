import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { CheckCircle2, Download, FileText, Archive } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Header */}
      <header className="border-b border-slate-700 bg-slate-900/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">RT</span>
              </div>
              <div>
                <h1 className="text-xl font-bold text-white">RT – Inversores</h1>
                <p className="text-xs text-slate-400">RGM Service</p>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Hero Section */}
        <div className="mb-12">
          <h2 className="text-4xl sm:text-5xl font-bold text-white mb-4">
            Checklist Técnico de Inversores
          </h2>
          <p className="text-lg text-slate-300 max-w-2xl">
            Sistema completo para inspeção, testes e manutenção de inversores de frequência com suporte a fotos, exportação de relatórios em PDF, TXT e ZIP.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          {/* Feature 1 */}
          <Card className="bg-slate-800/50 border-slate-700 p-6 hover:border-orange-500/50 transition-colors">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 bg-orange-500/10 rounded-lg flex items-center justify-center flex-shrink-0">
                <CheckCircle2 className="w-6 h-6 text-orange-500" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">Checklist Interativo</h3>
                <p className="text-sm text-slate-400">
                  8 seções completas com mais de 100 itens de verificação para análise abrangente.
                </p>
              </div>
            </div>
          </Card>

          {/* Feature 2 */}
          <Card className="bg-slate-800/50 border-slate-700 p-6 hover:border-orange-500/50 transition-colors">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 bg-orange-500/10 rounded-lg flex items-center justify-center flex-shrink-0">
                <FileText className="w-6 h-6 text-orange-500" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">Exportação Múltipla</h3>
                <p className="text-sm text-slate-400">
                  Gere relatórios em PDF, TXT e HTML com formatação profissional.
                </p>
              </div>
            </div>
          </Card>

          {/* Feature 3 */}
          <Card className="bg-slate-800/50 border-slate-700 p-6 hover:border-orange-500/50 transition-colors">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 bg-orange-500/10 rounded-lg flex items-center justify-center flex-shrink-0">
                <Archive className="w-6 h-6 text-orange-500" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-white mb-2">Suporte a Fotos</h3>
                <p className="text-sm text-slate-400">
                  Adicione fotos de cada item e exporte tudo em um arquivo ZIP organizado.
                </p>
              </div>
            </div>
          </Card>
        </div>

        {/* CTA Section */}
        <div className="bg-gradient-to-r from-orange-500/10 to-orange-600/10 border border-orange-500/20 rounded-lg p-8 mb-12">
          <h3 className="text-2xl font-bold text-white mb-4">Pronto para começar?</h3>
          <p className="text-slate-300 mb-6 max-w-2xl">
            Acesse o checklist completo com todas as funcionalidades de inspeção, testes e geração de relatórios.
          </p>
          <a href="/checklist.html" target="_blank" rel="noopener noreferrer">
            <Button className="bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white font-semibold px-8 py-6 text-lg rounded-lg">
              <Download className="w-5 h-5 mr-2" />
              Abrir Checklist
            </Button>
          </a>
        </div>

        {/* Features List */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h3 className="text-xl font-bold text-white mb-6">Funcionalidades Principais</h3>
            <ul className="space-y-4">
              {[
                "Análise Inicial – Medições Estáticas",
                "Condição na Bancada de Testes",
                "Testes de Partes e Peças",
                "Defeito Encontrado",
                "Reparo / Manutenção Preventiva",
                "Testes Finais de Validação",
                "Possível Causa da Falha",
                "Recomendações Técnicas",
              ].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-slate-300">
                  <div className="w-2 h-2 bg-orange-500 rounded-full" />
                  {item}
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-xl font-bold text-white mb-6">Recursos Técnicos</h3>
            <ul className="space-y-4">
              {[
                "Suporte a PWA (Progressive Web App)",
                "Funciona offline com localStorage",
                "Captura de fotos com câmera do dispositivo",
                "Exportação em PDF com imagens",
                "Exportação em TXT com formatação",
                "Salvamento em ZIP com fotos organizadas",
                "Compatibilidade com Android e iOS",
                "Interface responsiva e intuitiva",
              ].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-slate-300">
                  <div className="w-2 h-2 bg-orange-500 rounded-full" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-700 bg-slate-900/50 mt-12 py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row justify-between items-center gap-4">
            <p className="text-sm text-slate-400">
              © 2025 RGM Service. Manutenção Eletrônica de Automação & Drives.
            </p>
            <p className="text-sm text-slate-400">
              Versão 2.0 - Todas as correções aplicadas
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
