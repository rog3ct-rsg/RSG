import re

path = '/home/ubuntu/upload/checklist_inversores_android-1(3)_fixed.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Usando concatenação de strings para evitar problemas com aspas triplas dentro de strings
save_zip_fixed = "  async function saveZip() {\n" + \
"    if (typeof JSZip === 'undefined') {\n" + \
"      alert('JSZip ainda carregando. Tente novamente em instantes.');\n" + \
"      return;\n" + \
"    }\n" + \
"\n" + \
"    // 1. Coletar estado\n" + \
"    const state = {\n" + \
"      os:       document.getElementById('campo-os').value,\n" + \
"      data:     document.getElementById('meta-data').value,\n" + \
"      obs:      document.getElementById('observacoes').value,\n" + \
"      checks:   [],\n" + \
"      inputs:   {},\n" + \
"      imgStore: {}\n" + \
"    };\n" + \
"\n" + \
"    document.querySelectorAll('.check-item').forEach(el => {\n" + \
"      state.checks.push(el.classList.contains('checked'));\n" + \
"    });\n" + \
"    document.querySelectorAll('input.outros-input[id]').forEach(el => {\n" + \
"      state.inputs[el.id] = el.value;\n" + \
"    });\n" + \
"\n" + \
"    const zip    = new JSZip();\n" + \
"    const fotos  = zip.folder('fotos');\n" + \
"\n" + \
"    // 2. Adicionar imagens ao ZIP\n" + \
"    Object.keys(imgStore).forEach(tid => {\n" + \
"      if (!imgStore[tid].length) return;\n" + \
"      state.imgStore[tid] = [];\n" + \
"      imgStore[tid].forEach((entry, idx) => {\n" + \
"        const parts = entry.dataUrl.split(',');\n" + \
"        const mime = (parts[0].match(/:(.*?);/) || [])[1] || 'image/jpeg';\n" + \
"        const ext = mime.split('/')[1] || 'jpg';\n" + \
"        const fileName = tid + '_' + idx + '.' + ext;\n" + \
"        \n" + \
"        fotos.file(fileName, parts[1], { base64: true });\n" + \
"        state.imgStore[tid].push({ name: entry.name, dataUrl: entry.dataUrl, fileName: 'fotos/' + fileName });\n" + \
"      });\n" + \
"    });\n" + \
"\n" + \
"    // 3. Gerar HTML limpo para o ZIP\n" + \
"    const stateJson = JSON.stringify(state).replace(/<\\/script>/gi, '<\\\\/script>');\n" + \
"    const restoreBlock = '<!-- ESTADO SALVO -->\\n' +\n" + \
"      '<script id=\"__rgm_state__\">\\n' +\n" + \
"      '(function(){\\n' +\n" + \
"      '  var S=' + stateJson + ';\\n' +\n" + \
"      '  function apply(){\\n' +\n" + \
"      '    var el;\\n' +\n" + \
"      '    el=document.getElementById(\\'campo-os\\');    if(el) el.value=S.os||\\'\\';\\n' +\n" + \
"      '    el=document.getElementById(\\'meta-data\\');   if(el&&S.data) el.value=S.data;\\n' +\n" + \
"      '    el=document.getElementById(\\'observacoes\\'); if(el) el.value=S.obs||\\'\\';\\n' +\n" + \
"      '    document.querySelectorAll(\\'.check-item\\').forEach(function(item,i){\\n' +\n" + \
"      '      if(!S.checks||!S.checks[i]) return;\\n' +\n" + \
"      '      item.classList.add(\\'checked\\');\\n' +\n" + \
"      '      var cb=item.querySelector(\\'input[type=\"checkbox\"]\\'); if(cb) cb.checked=true;\\n' +\n" + \
"      '      var wrap=item.closest(\\'.check-wrap\\');\\n' +\n" + \
"      '      if(wrap){var p=wrap.querySelector(\\'.img-panel\\');if(p)p.classList.add(\\'open\\');}\\n' +\n" + \
"      '    });\\n' +\n" + \
"      '    Object.keys(S.inputs||{}).forEach(function(id){\\n' +\n" + \
"      '      el=document.getElementById(id); if(el) el.value=S.inputs[id];\\n' +\n" + \
"      '    });\\n' +\n" + \
"      '    Object.keys(S.imgStore||{}).forEach(function(tid){\\n' +\n" + \
"      '      var entries=S.imgStore[tid];\\n' +\n" + \
"      '      if(!entries||!entries.length) return;\\n' +\n" + \
"      '      var thumbsEl=document.getElementById(tid); if(!thumbsEl) return;\\n' +\n" + \
"      '      if(!window.imgStore) window.imgStore={};\\n' +\n" + \
"      '      window.imgStore[tid]=[];\\n' +\n" + \
"      '      entries.forEach(function(e){\\n' +\n" + \
"      '        var entry={name:e.name,dataUrl:e.dataUrl};\\n' +\n" + \
"      '        window.imgStore[tid].push(entry);\\n' +\n" + \
"      '        var wrap=document.createElement(\\'div\\'); wrap.className=\\'img-thumb-wrap\\';\\n' +\n" + \
"      '        var img=document.createElement(\\'img\\'); img.src=entry.dataUrl;\\n' +\n" + \
"      '        var del=document.createElement(\\'button\\'); del.className=\\'img-thumb-del\\'; del.textContent=\\'✕\\';\\n' +\n" + \
"      '        del.onclick=function(ev){\\n' +\n" + \
"      '          ev.stopPropagation();\\n' +\n" + \
"      '          var idx=window.imgStore[tid].indexOf(entry);\\n' +\n" + \
"      '          if(idx>-1)window.imgStore[tid].splice(idx,1);\\n' +\n" + \
"      '          wrap.remove();\\n' +\n" + \
"      '        };\\n' +\n" + \
"      '        wrap.appendChild(img); wrap.appendChild(del);\\n' +\n" + \
"      '        thumbsEl.appendChild(wrap);\\n' +\n" + \
"      '      });\\n' +\n" + \
"      '    });\\n' +\n" + \
"      '    if(typeof updateProgress===\\'function\\') updateProgress();\\n' +\n" + \
"      '  }\\n' +\n" + \
"      '  if(document.readyState===\\'loading\\'){document.addEventListener(\\'DOMContentLoaded\\',apply);}else{apply();}\\n' +\n" + \
"      '})();\\n' +\n" + \
"      '</' + 'script>\\n' +\n" + \
"      '<!-- FIM ESTADO -->';\n" + \
"\n" + \
"    let htmlBase = '<!DOCTYPE html>\\n' + document.documentElement.outerHTML;\n" + \
"    htmlBase = htmlBase.replace(/<!-- ESTADO SALVO -->[\\s\\S]*?<!-- FIM ESTADO -->\\n?/g, '');\n" + \
"    \n" + \
"    const insertAt = htmlBase.lastIndexOf('</body>');\n" + \
"    const finalHtml = insertAt !== -1\n" + \
"      ? htmlBase.slice(0, insertAt) + restoreBlock + '\\n' + htmlBase.slice(insertAt)\n" + \
"      : htmlBase + restoreBlock;\n" + \
"\n" + \
"    const osNum    = (state.os || 'RT').replace(/[^a-zA-Z0-9_-]/g, '_');\n" + \
"    const d        = (state.data || '').replace(/-/g, '');\n" + \
"    const baseName = 'RT_Inversores_' + osNum + (d ? '_' + d : '');\n" + \
"\n" + \
"    zip.file(baseName + '.html', finalHtml);\n" + \
"\n" + \
"    const zipBlob = await zip.generateAsync({\n" + \
"      type: 'blob',\n" + \
"      compression: 'DEFLATE',\n" + \
"      compressionOptions: { level: 6 }\n" + \
"    });\n" + \
"\n" + \
"    const zipFile = new File([zipBlob], baseName + '.zip', { type: 'application/zip' });\n" + \
"\n" + \
"    if (navigator.share && navigator.canShare && navigator.canShare({ files: [zipFile] })) {\n" + \
"      navigator.share({ files: [zipFile], title: baseName + '.zip' }).catch(dlFallback);\n" + \
"    } else { dlFallback(); }\n" + \
"\n" + \
"    function dlFallback() {\n" + \
"      const url = URL.createObjectURL(zipBlob);\n" + \
"      const a   = document.createElement('a');\n" + \
"      a.href = url; a.download = baseName + '.zip';\n" + \
"      document.body.appendChild(a); a.click();\n" + \
"      setTimeout(() => { document.body.removeChild(a); URL.revokeObjectURL(url); }, 300);\n" + \
"    }\n" + \
"  }";

start_marker = "async function saveZip() {"
restaurar_marker = "  // ── RESTAURAR"

start_idx = content.find(start_marker)
if start_idx != -1:
    end_idx = content.find(restaurar_marker, start_idx)
    if end_idx != -1:
        new_content = content[:start_idx] + save_zip_fixed + "\n\n" + content[end_idx:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Sucesso")
    else:
        print("Marcador de restauração não encontrado")
else:
    print("Função saveZip não encontrada")
