/**
 * Copyright 2023 Progress Software Corporation and/or one of its subsidiaries or affiliates. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
(function (factory) {
  typeof define === 'function' && define.amd ? define(['kendo.core'], factory) :
  factory();
})((function () {
  (function($, undefined$1) {

  /* Mensagens ColorGradient */

  if (kendo.ui.ColorGradient) {
      kendo.ui.ColorGradient.prototype.options.messages =
      $.extend(true, kendo.ui.ColorGradient.prototype.options.messages,{
          "contrastRatio": "Rácio de contraste:",
          "fail": "Falha",
          "pass": "Passar",
          "hex": "HEX",
          "toggleFormat": "Alternar formato",
          "red": "Vermelho",
          "green": "Verde",
          "blue": "Azul",
          "alpha": "Alfa"
      });
  }

  /* Mensagens FlatColorPicker */

  if (kendo.ui.FlatColorPicker) {
  kendo.ui.FlatColorPicker.prototype.options.messages =
  $.extend(true, kendo.ui.FlatColorPicker.prototype.options.messages,{
    "apply": "Aplicar",
    "cancel": "Cancelar",
    "noColor": "sem cor",
    "clearColor": "Limpar cor"
  });
  }

  /* Mensagens ColorPicker */

  if (kendo.ui.ColorPicker) {
  kendo.ui.ColorPicker.prototype.options.messages =
  $.extend(true, kendo.ui.ColorPicker.prototype.options.messages,{
    "apply": "Aplicar",
    "cancel": "Cancelar",
    "noColor": "sem cor",
    "clearColor": "Limpar cor"
  });
  }

  /* Mensagens ColumnMenu */

  if (kendo.ui.ColumnMenu) {
  kendo.ui.ColumnMenu.prototype.options.messages =
  $.extend(true, kendo.ui.ColumnMenu.prototype.options.messages,{
    "sortAscending": "Ordenar Ascendente",
    "sortDescending": "Ordenar Descendente",
    "filter": "Filtrar",
    "column": "Coluna",
    "columns": "Colunas",
    "columnVisibility": "Visibilidade da Coluna",
    "clear": "Limpar",
    "cancel": "Cancelar",
    "done": "Concluído",
    "settings": "Editar Configurações da Coluna",
    "lock": "Bloquear Coluna",
    "unlock": "Desbloquear Coluna",
    "stick": "Fixar Coluna",
    "unstick": "Desafixar Coluna",
    "setColumnPosition": "Definir Posição da Coluna",
    "apply": "Aplicar",
    "reset": "Redefinir",
    "buttonTitle": "{0} editar configurações da coluna",
    "movePrev": "Mover anterior",
    "moveNext": "Mover seguinte",
    "groupColumn": "Agrupar coluna",
    "ungroupColumn": "Desagrupar coluna"
  });
  }

  /* Mensagens DateRangePicker */

  if (kendo.ui.DateRangePicker) {
  kendo.ui.DateRangePicker.prototype.options.messages =
  $.extend(true, kendo.ui.DateRangePicker.prototype.options.messages,{
    "startLabel": "Início",
    "endLabel": "Fim"
  });
  }

  /* Mensagens Editor */

  if (kendo.ui.Editor) {
  kendo.ui.Editor.prototype.options.messages =
  $.extend(true, kendo.ui.Editor.prototype.options.messages,{
    "auto": "Automático",
    "bold": "Negrito",
    "italic": "Itálico",
    "search": "Procurar",
    "dropFilesHere": "Arraste os ficheiros aqui.",
    "underline": "Sublinhado",
    "strikethrough": "Rasurado",
    "superscript": "Superior",
    "subscript": "Inferior",
    "justifyCenter": "Centrar texto",
    "justifyLeft": "Alinhar texto à esquerda",
    "justifyRight": "Alinhar texto à direita",
    "justifyFull": "Justificar",
    "insertUnorderedList": "Inserir lista não ordenada",
    "insertOrderedList": "Inserir lista ordenada",
    "indent": "Avançar",
    "outdent": "Recuar",
    "createLink": "Inserir hiperligação",
    "unlink": "Remover hiperligação",
    "insertImage": "Inserir imagem",
    "insertFile": "Inserir ficheiro",
    "insertHtml": "Inserir HTML",
    "viewHtml": "Ver HTML",
    "fontName": "Selecionar família de fontes",
    "fontNameInherit": "(herdada)",
    "fontSize": "Selecionar tamanho da fonte",
    "fontSizeInherit": "(tamanho herdado)",
    "formatBlock": "Formatar",
    "formatting": "Formatar",
    "foreColor": "Cor",
    "backColor": "Cor de fundo",
    "style": "Estilos",
    "emptyFolder": "Pasta vazia",
    "uploadFile": "Enviar Ficheiro",
    "overflowAnchor": "Mais ferramentas",
    "orderBy": "Organizar por:",
    "orderBySize": "Tamanho",
    "orderByName": "Nome",
    "invalidFileType": "O ficheiro selecionado \"{0}\" não é válido. Os tipos de ficheiro suportados são {1}.",
    "deleteFile": 'Tem a certeza de que deseja eliminar "{0}"?',
    "overwriteFile": 'Já existe um ficheiro com o nome "{0}" no diretório atual. Deseja substituí-lo?',
    "directoryNotFound": "Um diretório com este nome não foi encontrado.",
    "imageWebAddress": "Endereço web",
    "imageAltText": "Texto alternativo",
    "imageWidth": "Largura (px)",
    "imageHeight": "Altura (px)",
    "fileWebAddress": "Endereço web",
    "fileTitle": "Título",
    "linkWebAddress": "Endereço web",
    "linkText": "Texto",
    "linkToolTip": "ToolTip",
    "linkOpenInNewWindow": "Abrir ligação numa nova janela",
    "dialogUpdate": "Atualizar",
    "dialogInsert": "Inserir",
    "dialogButtonSeparator": "ou",
    "dialogCancel": "Cancelar",
    "cleanFormatting": "Limpar formatação",
    "createTable": "Criar tabela",
    "addColumnLeft": "Adicionar coluna à esquerda",
    "addColumnRight": "Adicionar coluna à direita",
    "addRowAbove": "Adicionar linha acima",
    "addRowBelow": "Adicionar linha abaixo",
    "deleteRow": "Eliminar linha",
    "deleteColumn": "Eliminar coluna",
    "dialogOk": "Confirmar",
    "tableBackground": "Fundo da tabela",
    "tableCellProperties": "Propriedades da célula",
    "tableProperties": "Propriedades da tabela",
    "tableWizard": "Assistente de Tabela",
    "tableTab": "Geral",
    "cellTab": "Célula",
    "accessibilityTab": "Avançado",
    "caption": "Legenda",
    "captionAlignment": "Alinhamento da legenda",
    "summary": "Resumo",
    "width": "Largura",
    "height": "Altura",
    "units": "Unidades",
    "cellSpacing": "Espaçamento de células",
    "cellPadding": "Preenchimento de células",
    "cellMargin": "Margem da célula",
    "alignment": "Alinhamento",
    "background": "Fundo",
    "cssClass": "Classe CSS",
    "id": "ID",
    "border": "Borda",
    "borderColor": "Cor da borda",
    "borderWidth": "Largura da borda",
    "borderStyle": "Estilo da borda",
    "collapseBorders": "Colapsar bordas",
    "wrapText": "Quebrar texto",
    "fitToCell": "Ajustar à célula",
    "associateCellsWithHeaders": "Associar cabeçalhos",
    "alignLeft": "Alinhar à esquerda",
    "alignCenter": "Alinhar ao centro",
    "alignRight": "Alinhar à direita",
    "alignLeftTop": "Alinhar à esquerda superior",
    "alignCenterTop": "Alinhar ao centro superior",
    "alignRightTop": "Alinhar à direita superior",
    "alignLeftMiddle": "Alinhar à esquerda ao meio",
    "alignCenterMiddle": "Alinhar ao centro ao meio",
    "alignRightMiddle": "Alinhar à direita ao meio",
    "alignLeftBottom": "Alinhar à esquerda inferior",
    "alignCenterBottom": "Alinhar ao centro inferior",
    "alignRightBottom": "Alinhar à direita inferior",
    "alignRemove": "Remover Alinhamento",
    "columns": "Colunas",
    "rows": "Linhas",
    "selectAllCells": "Aplicar a todas as células",
    "applyToColumn": "aplicar à coluna",
    "applyToRow": "aplicar à linha",
    "print": "Imprimir",
    "headerRows": "Linhas de Cabeçalho",
    "headerColumns": "Colunas de Cabeçalho",
    "tableSummaryPlaceholder": "O atributo de resumo não é compatível com o HTML5.",
    "associateNone": "Nenhum",
    "associateScope": "Associar usando o atributo 'scope'",
    "associateIds": "Associar usando IDs",
    "copyFormat": "Copiar formato",
    "applyFormat": "Aplicar formato",
    "borderNone": "Nenhum",
    "undo": "Desfazer",
    "redo": "Refazer"
  });
  }

  /* Mensagens FileBrowser */

  if (kendo.ui.FileBrowser) {
  kendo.ui.FileBrowser.prototype.options.messages =
  $.extend(true, kendo.ui.FileBrowser.prototype.options.messages,{
    "uploadFile": "Enviar Ficheiro",
    "orderBy": "Ordenar por",
    "orderByName": "Nome",
    "orderBySize": "Tamanho",
    "directoryNotFound": "Um diretório com este nome não foi encontrado.",
    "emptyFolder": "Pasta vazia",
    "deleteFile": 'Tem a certeza de que deseja eliminar "{0}"?',
    "invalidFileType": "O ficheiro selecionado \"{0}\" não é válido. Os tipos de ficheiro suportados são {1}.",
    "overwriteFile": "Já existe um ficheiro com o nome \"{0}\" no diretório atual. Deseja substituí-lo?",
    "dropFilesHere": "arraste o ficheiro aqui para enviar",
    "search": "Procurar"
  });
  }

  /* Mensagens FileManager */

  if (kendo.ui.FileManager) {
      kendo.ui.FileManager.prototype.options.messages =
      $.extend(true, kendo.ui.FileManager.prototype.options.messages,{
          toolbar: {
              createFolder: "Nova Pasta",
              upload: "Enviar Ficheiro",
              sortDirection: "Direção de Ordenação",
              sortDirectionAsc: "Direção de Ordenação Ascendente",
              sortDirectionDesc: "Direção de Ordenação Descendente",
              sortField: "Ordenar Por",
              nameField: "Nome",
              sizeField: "Tamanho do Ficheiro",
              typeField: "Tipo",
              dateModifiedField: "Data de Modificação",
              dateCreatedField: "Data de Criação",
              listView: "Vista de Lista",
              gridView: "Vista de Grelha",
              search: "Procurar",
              details: "Ver Detalhes",
              detailsChecked: "On",
              detailsUnchecked: "Off",
              "delete": "Eliminar",
              rename: "Renomear"
          },
          views: {
              nameField: "Nome",
              sizeField: "Tamanho do Ficheiro",
              typeField: "Tipo",
              dateModifiedField: "Data de Modificação",
              dateCreatedField: "Data de Criação",
              items: "itens",
              listLabel: "Vista de Lista do Gestor de Ficheiros",
              gridLabel: "Vista de Grelha do Gestor de Ficheiros",
              treeLabel: "Vista de Árvore do Gestor de Ficheiros"
          },
          dialogs: {
              upload: {
                  title: "Enviar Ficheiros",
                  clear: "Limpar Lista",
                  done: "Concluído"
              },
              moveConfirm: {
                  title: "Confirmar",
                  content: "<p class='k-text-center'>Deseja mover ou copiar?</p>",
                  okText: "Copiar",
                  cancel: "Mover",
                  close: "fechar"
              },
              deleteConfirm: {
                  title: "Confirmar",
                  content: "<p class='k-text-center'>Tem a certeza de que deseja eliminar o(s) ficheiro(s) selecionado(s)?<br/>Não pode desfazer esta ação.</p>",
                  okText: "Eliminar",
                  cancel: "Cancelar",
                  close: "fechar"
              },
              renamePrompt: {
                  title: "Prompt",
                  content: "<p class='k-text-center'>Introduza um novo nome para o ficheiro.</p>",
                  okText: "Renomear",
                  cancel: "Cancelar",
                  close: "fechar"
              }
          },
          previewPane: {
              noFileSelected: "Nenhum Ficheiro Selecionado",
              extension: "Tipo",
              size: "Tamanho",
              created: "Data de Criação",
              createdUtc: "Data de Criação UTC",
              modified: "Data de Modificação",
              modifiedUtc: "Data de Modificação UTC",
              items: "itens"
          }
      });
  }

  /* Mensagens do FilterCell */

if (kendo.ui.FilterCell) {
  kendo.ui.FilterCell.prototype.options.messages =
  $.extend(true, kendo.ui.FilterCell.prototype.options.messages,{
    "isTrue": "é verdadeiro",
    "isFalse": "é falso",
    "filter": "Filtrar",
    "clear": "Limpar",
    "operator": "Operador"
  });
}

/* Operadores do FilterCell */

if (kendo.ui.FilterCell) {
  kendo.ui.FilterCell.prototype.options.operators =
  $.extend(true, kendo.ui.FilterCell.prototype.options.operators,{
    "string": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "startswith": "Começa com",
      "contains": "Contém",
      "doesnotcontain": "Não contém",
      "endswith": "Termina com",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo",
      "isempty": "Está vazio",
      "isnotempty": "Não está vazio",
      "isnullorempty": "Não tem valor",
      "isnotnullorempty": "Tem valor"
    },
    "number": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "gte": "É maior ou igual a",
      "gt": "É maior que",
      "lte": "É menor ou igual a",
      "lt": "É menor que",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo"
    },
    "date": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "gte": "É depois ou igual a",
      "gt": "É depois de",
      "lte": "É antes ou igual a",
      "lt": "É antes de",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo"
    },
    "enums": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo"
    }
  });
}

/* Mensagens do FilterMenu */

if (kendo.ui.FilterMenu) {
  kendo.ui.FilterMenu.prototype.options.messages =
  $.extend(true, kendo.ui.FilterMenu.prototype.options.messages,{
    "info": "Mostrar itens com valor que:",
    "title": "Mostrar itens com valor que",
    "isTrue": "é verdadeiro",
    "isFalse": "é falso",
    "filter": "Filtrar",
    "clear": "Limpar",
    "and": "E",
    "or": "Ou",
    "selectValue": "-Selecionar valor-",
    "operator": "Operador",
    "value": "Valor",
    "cancel": "Cancelar",
    "done": "Concluído",
    "into": "em",
    "buttonTitle": "Configurações da coluna de filtro {0}"
  });
}

/* Mensagens do operador do FilterMenu */

if (kendo.ui.FilterMenu) {
  kendo.ui.FilterMenu.prototype.options.operators =
  $.extend(true, kendo.ui.FilterMenu.prototype.options.operators,{
    "string": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "startswith": "Começa com",
      "contains": "Contém",
      "doesnotcontain": "Não contém",
      "endswith": "Termina com",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo",
      "isempty": "Está vazio",
      "isnotempty": "Não está vazio",
      "isnullorempty": "Não tem valor",
      "isnotnullorempty": "Tem valor"
    },
    "number": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "gte": "É maior ou igual a",
      "gt": "É maior que",
      "lte": "É menor ou igual a",
      "lt": "É menor que",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo"
    },
    "date": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "gte": "É depois ou igual a",
      "gt": "É depois de",
      "lte": "É antes ou igual a",
      "lt": "É antes de",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo"
    },
    "enums": {
      "eq": "É igual a",
      "neq": "Não é igual a",
      "isnull": "É nulo",
      "isnotnull": "Não é nulo"
    }
  });
}

/* Mensagens do FilterMultiCheck */

if (kendo.ui.FilterMultiCheck) {
  kendo.ui.FilterMultiCheck.prototype.options.messages =
  $.extend(true, kendo.ui.FilterMultiCheck.prototype.options.messages,{
    "checkAll": "Selecionar Todos",
    "clearAll": "Limpar Todos",
    "clear": "Limpar",
    "filter": "Filtrar",
    "search": "Buscar",
    "cancel": "Cancelar",
    "selectedItemsFormat": "{0} itens selecionados",
    "done": "Concluído",
    "into": "em"
  });
}

/* Mensagens do Gantt */

if (kendo.ui.Gantt) {
  kendo.ui.Gantt.prototype.options.messages =
  $.extend(true, kendo.ui.Gantt.prototype.options.messages,{
    "actions": {
      "addChild": "Adicionar Filho",
      "append": "Adicionar Tarefa",
      "insertAfter": "Adicionar Abaixo",
      "insertBefore": "Adicionar Acima",
      "pdf": "Exportar para PDF"
    },
    "cancel": "Cancelar",
    "deleteDependencyWindowTitle": "Excluir dependência",
    "deleteTaskWindowTitle": "Excluir tarefa",
    "destroy": "Excluir",
    "editor": {
      "assingButton": "Atribuir",
      "editorTitle": "Tarefa",
      "end": "Fim",
      "percentComplete": "Completo",
      "plannedStart": "Início Planejado",
      "plannedEnd": "Fim Planejado",
      "resources": "Recursos",
      "resourcesEditorTitle": "Recursos",
      "resourcesHeader": "Recursos",
      "start": "Início",
      "title": "Título",
      "unitsHeader": "Unidades",
      "parent": "Pai",
      "addNew": "Adicionar",
      "name": "Nome",
      "percentCompleteHint": "valor de 0 a 1",
      "remove": "Remover",
      "actualStart": "Início Real",
      "actualEnd": "Fim Real",
      "parentOptionLabel": "-Nenhum-",
      "general": "Geral",
      "predecessors": "Predecessores",
      "successors": "Sucessores",
      "other": "Outro",
      "dependencyType": "Tipo"
    },
    "plannedTasks": {
      "switchText": "Tarefas Planejadas",
      "offsetTooltipAdvanced": "Cumprido antes do prazo",
      "offsetTooltipDelay": "Atraso",
      "seconds": "segundos",
      "minutes": "minutos",
      "hours": "horas",
      "days": "dias"
    },
    "save": "Salvar",
    "selectView": "Selecionar visualização",
    "views": {
      "day": "Dia",
      "end": "Fim",
      "month": "Mês",
      "start": "Início",
      "week": "Semana",
      "year": "Ano"
    }
  });
}

/* Mensagens do Grid */

if (kendo.ui.Grid) {
  kendo.ui.Grid.prototype.options.messages =
  $.extend(true, kendo.ui.Grid.prototype.options.messages,{
    "commands": {
      "cancel": "Cancelar alterações",
      "canceledit": "Cancelar",
      "create": "Adicionar novo registro",
      "destroy": "Excluir",
      "edit": "Editar",
      "excel": "Exportar para Excel",
      "pdf": "Exportar para PDF",
      "save": "Salvar alterações",
      "select": "Selecionar",
      "update": "Salvar",
      "search": "Buscar...",
      "selectRow": "Selecionar Linha",
      "selectAllRows": "Todas as linhas",
      "clearSelection": "Limpar seleção",
      "copySelection": "Copiar seleção",
      "copySelectionNoHeaders": "Copiar seleção (Sem Cabeçalhos)",
      "reorderRow": "Reordenar linha",
      "reorderRowUp": "Acima",
      "reorderRowDown": "Abaixo",
      "reorderRowTop": "Topo",
      "reorderRowBottom": "Fundo",
      "exportPdf": "Exportar para PDF",
      "exportExcel": "Exportar para Excel",
      "exportToExcelAll": "Todos",
      "exportToExcelSelection": "Seleção",
      "exportToExcelSelectionNoHeaders": "Seleção (Sem Cabeçalhos)",
      "sortAsc": "Ordenar Ascendente",
      "sortDesc": "Ordenar Descendente",
      "moveGroupPrevious": "Mover anterior",
      "moveGroupNext": "Mover próximo",
    },
    "editable": {
      "cancelDelete": "Cancelar",
      "confirmation": "Tem certeza de que deseja excluir este registro?",
      "confirmDelete": "Excluir"
    },
    "noRecords": "Nenhum registro disponível.",
    "expandCollapseColumnHeader": "",
    "groupHeader": "Pressione ctrl + espaço para agrupar",
    "ungroupHeader": "Pressione ctrl + espaço para desagrupar",
    "toolbarLabel": "barra de ferramentas do grid",
    "groupingHeaderLabel": "cabeçalho de agrupamento do grid",
    "filterCellTitle": "célula de filtro"
  });
}


  /* Mensagens do TaskBoard */

if (kendo.ui.TaskBoard) {
  kendo.ui.TaskBoard.prototype.options.messages =
  $.extend(true, kendo.ui.TaskBoard.prototype.options.messages,{
      "edit": "Editar",
      "createNewCard": "Criar novo cartão",
      "create": "Criar",
      "search": "Buscar",
      "previewCard": "Visualizar cartão",
      "addCard": "Adicionar cartão",
      "editCard": "Editar cartão",
      "deleteCard": "Excluir cartão",
      "addColumn": "Adicionar coluna",
      "editColumn": "Editar coluna",
      "deleteColumn": "Excluir coluna",
      "close": "Fechar",
      "cancel": "Cancelar",
      "delete": "Excluir",
      "saveChanges": "Salvar alterações",
      "title": "Título:",
      "description": "Descrição:",
      "newColumn": "Nova coluna",
      "deleteColumnConfirm": "Tem certeza de que deseja excluir esta coluna?",
      "deleteCardConfirm": "Tem certeza de que deseja excluir este cartão?"
  });
}

/* Mensagens do TreeList */

if (kendo.ui.TreeList) {
  kendo.ui.TreeList.prototype.options.messages =
  $.extend(true, kendo.ui.TreeList.prototype.options.messages,{
      "noRows": "Nenhum registro para exibir",
      "loading": "Carregando...",
      "requestFailed": "Falha na solicitação.",
      "retry": "Tentar novamente",
      "commands": {
          "edit": "Editar",
          "update": "Salvar",
          "canceledit": "Cancelar",
          "create": "Adicionar novo registro",
          "createchild": "Adicionar registro filho",
          "destroy": "Excluir",
          "excel": "Exportar para Excel",
          "pdf": "Exportar para PDF"
      }
  });
}

/* Mensagens do Groupable */

if (kendo.ui.Groupable) {
  kendo.ui.Groupable.prototype.options.messages =
  $.extend(true, kendo.ui.Groupable.prototype.options.messages,{
    "empty": "Arraste um cabeçalho de coluna e solte aqui para agrupar por essa coluna"
  });
}

/* Mensagens do NumericTextBox */

if (kendo.ui.NumericTextBox) {
  kendo.ui.NumericTextBox.prototype.options =
  $.extend(true, kendo.ui.NumericTextBox.prototype.options,{
    "upArrowText": "Aumentar valor",
    "downArrowText": "Diminuir valor"
  });
}

/* Mensagens do MediaPlayer */

if (kendo.ui.MediaPlayer) {
  kendo.ui.MediaPlayer.prototype.options.messages =
  $.extend(true, kendo.ui.MediaPlayer.prototype.options.messages,{
    "pause": "Pausar",
    "play": "Reproduzir",
    "mute": "Silenciar",
    "unmute": "Ativar som",
    "quality": "Qualidade",
    "fullscreen": "Tela cheia",
    "volume": "Volume",
    "time": "Tempo"
  });
}

/* Mensagens do Pager */

if (kendo.ui.Pager) {
  kendo.ui.Pager.prototype.options.messages =
  $.extend(true, kendo.ui.Pager.prototype.options.messages,{
    "allPages": "Todos",
    "display": "{0} - {1} de {2} itens",
    "empty": "Nenhum item para exibir",
    "page": "Página",
    "pageButtonLabel": "Página {0}",
    "pageSizeDropDownLabel": "Tamanhos de página",
    "of": "de {0}",
    "itemsPerPage": "itens por página",
    "first": "Ir para a primeira página",
    "previous": "Ir para a página anterior",
    "next": "Ir para a próxima página",
    "last": "Ir para a última página",
    "refresh": "Atualizar",
    "morePages": "Mais páginas"
  });
}

/* Mensagens do TreeListPager */

if (kendo.ui.TreeListPager) {
  kendo.ui.TreeListPager.prototype.options.messages =
  $.extend(true, kendo.ui.TreeListPager.prototype.options.messages,{
    "allPages": "Todos",
    "display": "{0} - {1} de {2} itens",
    "empty": "Nenhum item para exibir",
    "page": "Página",
    "of": "de {0}",
    "itemsPerPage": "itens por página",
    "first": "Ir para a primeira página",
    "previous": "Ir para a página anterior",
    "next": "Ir para a próxima página",
    "last": "Ir para a última página",
    "refresh": "Atualizar",
    "morePages": "Mais páginas"
  });
}

/* Mensagens do PivotGrid */

if (kendo.ui.PivotGrid) {
  kendo.ui.PivotGrid.prototype.options.messages =
  $.extend(true, kendo.ui.PivotGrid.prototype.options.messages,{
    "measureFields": "Solte os Campos de Dados Aqui",
    "columnFields": "Solte os Campos de Coluna Aqui",
    "rowFields": "Solte os Campos de Linha Aqui"
  });
}

/* Mensagens do PivotFieldMenu */

if (kendo.ui.PivotFieldMenu) {
  kendo.ui.PivotFieldMenu.prototype.options.messages =
  $.extend(true, kendo.ui.PivotFieldMenu.prototype.options.messages,{
    "info": "Mostrar itens com valor que:",
    "filterFields": "Filtros de Campos",
    "filter": "Filtrar",
    "include": "Incluir Campos...",
    "title": "Campos a incluir",
    "clear": "Limpar",
    "ok": "Ok",
    "cancel": "Cancelar",
    "operators": {
      "contains": "Contém",
      "doesnotcontain": "Não contém",
      "startswith": "Começa com",
      "endswith": "Termina com",
      "eq": "É igual a",
      "neq": "Não é igual a"
    }
  });
}

/* Mensagens do RecurrenceEditor */

if (kendo.ui.RecurrenceEditor) {
  kendo.ui.RecurrenceEditor.prototype.options.messages =
  $.extend(true, kendo.ui.RecurrenceEditor.prototype.options.messages,{
    "repeat": "Repetir",
    "recurrenceEditorTitle": "Editor de Recorrência",
    "frequencies": {
      "never": "Nunca",
      "hourly": "A cada hora",
      "daily": "Diariamente",
      "weekly": "Semanalmente",
      "monthly": "Mensalmente",
      "yearly": "Anualmente"
    },
    "hourly": {
      "repeatEvery": "Repetir a cada: ",
      "interval": " hora(s)"
    },
    "daily": {
      "repeatEvery": "Repetir a cada: ",
      "interval": " dia(s)"
    },
    "weekly": {
      "interval": " semana(s)",
      "repeatEvery": "Repetir a cada: ",
      "repeatOn": "Repetir em: "
    },
    "monthly": {
      "repeatEvery": "Repetir a cada: ",
      "repeatOn": "Repetir em: ",
      "interval": " mês(es)",
      "day": "Dia ",
      "date": "Data"
    },
    "yearly": {
      "repeatEvery": "Repetir a cada: ",
      "repeatOn": "Repetir em: ",
      "interval": " ano(s)",
      "of": " de ",
      "month": "mês",
      "day": "dia",
      "date": "Data"
    },
    "end": {
      "label": "Fim:",
      "mobileLabel": "Termina",
      "never": "Nunca",
      "after": "Depois de ",
      "occurrence": " ocorrência(s)",
      "on": "Em "
    },
    "offsetPositions": {
      "first": "primeiro",
      "second": "segundo",
      "third": "terceiro",
      "fourth": "quarto",
      "last": "último"
    },
    "weekdays": {
      "day": "dia",
      "weekday": "dia da semana",
      "weekend": "fim de semana"
    }
  });
}


  /* Mensagens do MobileRecurrenceEditor */

if (kendo.ui.MobileRecurrenceEditor) {
  kendo.ui.MobileRecurrenceEditor.prototype.options.messages =
  $.extend(true, kendo.ui.MobileRecurrenceEditor.prototype.options.messages, kendo.ui.RecurrenceEditor.prototype.options.messages, {
    "cancel": "Cancelar",
    "update": "Salvar",
    "endTitle": "Repetição termina",
    "repeatTitle": "Padrão de repetição",
    "headerTitle": "Repetir evento",
    "end": {
      "patterns": {
        "never": "Nunca",
        "after": "Depois...",
        "on": "Em..."
      },
      "never": "Nunca",
      "after": "Repetir após",
      "on": "Repetir em"
    },
    "daily": {
      "interval": ""
    },
    "hourly": {
      "interval": ""
    },
    "weekly": {
      "interval": ""
    },
    "monthly": {
      "interval": "",
      "repeatBy": "Repetir por: ",
      "dayOfMonth": "Dia do mês",
      "dayOfWeek": "Dia da semana",
      "repeatEvery": "Repetir a cada",
      "every": "Cada",
      "day": "Dia "
    },
    "yearly": {
      "interval": "",
      "repeatBy": "Repetir por: ",
      "dayOfMonth": "Dia do mês",
      "dayOfWeek": "Dia da semana",
      "repeatEvery": "Repetir a cada: ",
      "every": "Cada",
      "month": "Mês",
      "day": "Dia"
    }
  });
}

/* Mensagens do Scheduler */

if (kendo.ui.Scheduler) {
  kendo.ui.Scheduler.prototype.options.messages =
  $.extend(true, kendo.ui.Scheduler.prototype.options.messages, {
    "allDay": "o dia todo",
    "date": "Data",
    "event": "Evento",
    "time": "Hora",
    "showFullDay": "Mostrar o dia completo",
    "showWorkDay": "Mostrar horas de trabalho",
    "today": "Hoje",
    "save": "Salvar",
    "cancel": "Cancelar",
    "destroy": "Excluir",
    "resetSeries": "Reiniciar Série",
    "deleteWindowTitle": "Excluir evento",
    "ariaSlotLabel": "Selecionado de {0:t} a {1:t}",
    "ariaEventLabel": "{0} em {1:D} às {2:t}",
    "refresh": "Atualizar",
    "selectView": "Selecionar visualização",
    "editable": {
      "confirmation": "Tem certeza de que deseja excluir este evento?"
    },
    "views": {
      "day": "Dia",
      "week": "Semana",
      "workWeek": "Semana de trabalho",
      "agenda": "Agenda",
      "month": "Mês"
    },
    "recurrenceMessages": {
      "deleteWindowTitle": "Excluir Item Recorrente",
      "resetSeriesWindowTitle": "Reiniciar Série",
      "deleteWindowOccurrence": "Excluir ocorrência atual",
      "deleteWindowSeries": "Excluir a série",
      "deleteRecurringConfirmation": "Tem certeza de que deseja excluir esta ocorrência de evento?",
      "deleteSeriesConfirmation": "Tem certeza de que deseja excluir toda a série?",
      "editWindowTitle": "Editar Item Recorrente",
      "editWindowOccurrence": "Editar ocorrência atual",
      "editWindowSeries": "Editar a série",
      "deleteRecurring": "Você deseja excluir apenas esta ocorrência de evento ou a série inteira?",
      "editRecurring": "Você deseja editar apenas esta ocorrência de evento ou a série inteira?"
    },
    "editor": {
      "title": "Título",
      "start": "Início",
      "end": "Fim",
      "allDayEvent": "Evento de dia inteiro",
      "description": "Descrição",
      "repeat": "Repetir",
      "timezone": " ",
      "startTimezone": "Fuso horário de início",
      "endTimezone": "Fuso horário de fim",
      "separateTimezones": "Usar fusos horários de início e fim separados",
      "timezoneEditorTitle": "Fusos Horários",
      "timezoneEditorButton": "Fuso horário",
      "timezoneTitle": "Fusos Horários",
      "noTimezone": "Sem fuso horário",
      "editorTitle": "Evento"
    },
    "search": "Buscar..."
  });
}

/* Mensagens do Spreadsheet */

if (kendo.spreadsheet && kendo.spreadsheet.messages.borderPalette) {
  kendo.spreadsheet.messages.borderPalette =
  $.extend(true, kendo.spreadsheet.messages.borderPalette, {
    "allBorders": "Todas as bordas",
    "insideBorders": "Bordas internas",
    "insideHorizontalBorders": "Bordas horizontais internas",
    "insideVerticalBorders": "Bordas verticais internas",
    "outsideBorders": "Bordas externas",
    "leftBorder": "Borda esquerda",
    "topBorder": "Borda superior",
    "rightBorder": "Borda direita",
    "bottomBorder": "Borda inferior",
    "noBorders": "Sem borda",
    "reset": "Redefinir cor",
    "customColor": "Cor personalizada...",
    "apply": "Aplicar",
    "cancel": "Cancelar"
  });
}

if (kendo.spreadsheet && kendo.spreadsheet.messages.dialogs) {
  kendo.spreadsheet.messages.dialogs =
  $.extend(true, kendo.spreadsheet.messages.dialogs, {
    "apply": "Aplicar",
    "save": "Salvar",
    "cancel": "Cancelar",
    "remove": "Remover",
    "retry": "Tentar novamente",
    "revert": "Reverter",
    "okText": "OK",
    "formatCellsDialog": {
      "title": "Formatar",
      "categories": {
        "number": "Número",
        "currency": "Moeda",
        "date": "Data"
      }
    },
    "fontFamilyDialog": {
      "title": "Fonte"
    },
    "fontSizeDialog": {
      "title": "Tamanho da Fonte"
    },
    "bordersDialog": {
      "title": "Bordas"
    },
    "alignmentDialog": {
      "title": "Alinhamento",
      "buttons": {
        "justifyLeft": "Alinhar à esquerda",
        "justifyCenter": "Centralizar",
        "justifyRight": "Alinhar à direita",
        "justifyFull": "Justificar",
        "alignTop": "Alinhar ao topo",
        "alignMiddle": "Alinhar ao meio",
        "alignBottom": "Alinhar à base"
      }
    },
    "mergeDialog": {
      "title": "Mesclar células",
      "buttons": {
        "mergeCells": "Mesclar tudo",
        "mergeHorizontally": "Mesclar horizontalmente",
        "mergeVertically": "Mesclar verticalmente",
        "unmerge": "Desmesclar"
      }
    },
    "freezeDialog": {
      "title": "Congelar painéis",
      "buttons": {
        "freezePanes": "Congelar painéis",
        "freezeRows": "Congelar linhas",
        "freezeColumns": "Congelar colunas",
        "unfreeze": "Descongelar painéis"
      }
    },
    "confirmationDialog": {
      "text": "Tem certeza de que deseja remover esta planilha?",
      "title": "Remover planilha"
    },
    "validationDialog": {
      "title": "Validação de dados",
      "hintMessage": "Digite um valor válido de {0} {1}.",
      "hintTitle": "Validação {0}",
      "criteria": {
        "any": "Qualquer valor",
        "number": "Número",
        "text": "Texto",
        "date": "Data",
        "custom": "Fórmula personalizada",
        "list": "Lista"
      },
      "comparers": {
        "greaterThan": "maior que",
        "lessThan": "menor que",
        "between": "entre",
        "notBetween": "não entre",
        "equalTo": "igual a",
        "notEqualTo": "não igual a",
        "greaterThanOrEqualTo": "maior ou igual a",
        "lessThanOrEqualTo": "menor ou igual a"
      },
      "comparerMessages": {
        "greaterThan": "maior que {0}",
        "lessThan": "menor que {0}",
        "between": "entre {0} e {1}",
        "notBetween": "não entre {0} e {1}",
        "equalTo": "igual a {0}",
        "notEqualTo": "não igual a {0}",
        "greaterThanOrEqualTo": "maior ou igual a {0}",
        "lessThanOrEqualTo": "menor ou igual a {0}",
        "custom": "que satisfaça a fórmula: {0}"
      },
      "labels": {
        "criteria": "Critério",
        "comparer": "Comparador",
        "min": "Mín",
        "max": "Máx",
        "value": "Valor",
        "start": "Início",
        "end": "Fim",
        "onInvalidData": "Em dados inválidos",
        "rejectInput": "Rejeitar entrada",
        "showWarning": "Mostrar aviso",
        "showHint": "Mostrar dica",
        "hintTitle": "Título da dica",
        "hintMessage": "Mensagem da dica",
        "ignoreBlank": "Ignorar células em branco"
      },
      "placeholders": {
        "typeTitle": "Título do tipo",
        "typeMessage": "Mensagem do tipo"
      }
    },
    "exportAsDialog": {
      "title": "Exportar...",
      "labels": {
        "fileName": "Nome do arquivo",
        "saveAsType": "Salvar como tipo",
        "exportArea": "Exportar",
        "paperSize": "Tamanho do papel",
        "margins": "Margens",
        "orientation": "Orientação",
        "print": "Imprimir",
        "guidelines": "Diretrizes",
        "center": "Centro",
        "horizontalmente": "Horizontalmente",
        "verticalmente": "Verticalmente"
      }
    },
    "modifyMergedDialog": {
      "errorMessage": "Não é possível alterar parte de uma célula mesclada."
    },
    "useKeyboardDialog": {
      "title": "Copiar e colar",
      "errorMessage": "Essas ações não podem ser executadas pelo menu. Use os atalhos de teclado em vez disso:",
      "labels": {
        "forCopy": "para copiar",
        "forCut": "para recortar",
        "forPaste": "para colar"
      }
    },
    "unsupportedSelectionDialog": {
      "errorMessage": "Essa ação não pode ser realizada em seleção múltipla."
    },
    "insertCommentDialog": {
      "title": "Inserir comentário",
      "labels": {
        "comment": "Comentário",
        "removeComment": "Remover comentário"
      }
    },
    "insertImageDialog": {
      "title": "Inserir imagem",
      "info": "Arraste uma imagem aqui ou clique para selecionar",
      "typeError": "Selecione uma imagem JPEG, PNG ou GIF"
    }
  });
}

if (kendo.spreadsheet && kendo.spreadsheet.messages.filterMenu) {
  kendo.spreadsheet.messages.filterMenu =
  $.extend(true, kendo.spreadsheet.messages.filterMenu, {
    "sortAscending": "Classificar de A a Z",
    "sortDescending": "Classificar de Z a A",
    "filterByValue": "Filtrar por valor",
    "filterByCondition": "Filtrar por condição",
    "apply": "Aplicar",
    "search": "Buscar",
    "addToCurrent": "Adicionar à seleção atual",
    "clear": "Limpar",
    "blanks": "(Em branco)",
    "operatorNone": "Nenhum",
    "and": "E",
    "or": "OU",
    "operators": {
      "string": {
        "contains": "Texto contém",
        "doesnotcontain": "Texto não contém",
        "startswith": "Texto começa com",
        "endswith": "Texto termina com"
      },
      "date": {
        "eq": "Data é",
        "neq": "Data não é",
        "lt": "Data é anterior a",
        "gt": "Data é posterior a"
      },
      "number": {
        "eq": "É igual a",
        "neq": "Não é igual a",
        "gte": "É maior ou igual a",
        "gt": "É maior que",
        "lte": "É menor ou igual a",
        "lt": "É menor que"
      }
    }
  });
}

if (kendo.spreadsheet && kendo.spreadsheet.messages.colorPicker) {
  kendo.spreadsheet.messages.colorPicker =
  $.extend(true, kendo.spreadsheet.messages.colorPicker, {
    "reset": "Redefinir cor",
    "customColor": "Cor personalizada...",
    "apply": "Aplicar",
    "cancel": "Cancelar"
  });
}

if (kendo.spreadsheet && kendo.spreadsheet.messages.toolbar) {
  kendo.spreadsheet.messages.toolbar =
  $.extend(true, kendo.spreadsheet.messages.toolbar,{
    "addColumnLeft": "Adicionar coluna à esquerda",
    "addColumnRight": "Adicionar coluna à direita",
    "addRowAbove": "Adicionar linha acima",
    "addRowBelow": "Adicionar linha abaixo",
    "alignment": "Alinhamento",
    "alignmentButtons": {
      "justifyLeft": "Alinhar à esquerda",
      "justifyCenter": "Centro",
      "justifyRight": "Alinhar à direita",
      "justifyFull": "Justificar",
      "alignTop": "Alinhar ao topo",
      "alignMiddle": "Alinhar ao meio",
      "alignBottom": "Alinhar à base"
    },
    "backgroundColor": "Fundo",
    "bold": "Negrito",
    "borders": "Bordas",
    "colorPicker": {
      "reset": "Redefinir cor",
      "customColor": "Cor personalizada..."
    },
    "copy": "Copiar",
    "cut": "Cortar",
    "deleteColumn": "Eliminar coluna",
    "deleteRow": "Eliminar linha",
    "excelImport": "Importar do Excel...",
    "filter": "Filtro",
    "fontFamily": "Fonte",
    "fontSize": "Tamanho da fonte",
    "format": "Formato personalizado...",
    "formatTypes": {
      "automatic": "Automático",
      "number": "Número",
      "percent": "Percentagem",
      "financial": "Financeiro",
      "currency": "Moeda",
      "date": "Data",
      "time": "Hora",
      "dateTime": "Data e hora",
      "duration": "Duração",
      "moreFormats": "Mais formatos..."
    },
    "formatDecreaseDecimal": "Diminuir casas decimais",
    "formatIncreaseDecimal": "Aumentar casas decimais",
    "freeze": "Fixar painéis",
    "freezeButtons": {
      "freezePanes": "Fixar painéis",
      "freezeRows": "Fixar linhas",
      "freezeColumns": "Fixar colunas",
      "unfreeze": "Desafixar painéis"
    },
    "insertComment": "Inserir comentário",
    "insertImage": "Inserir imagem",
    "italic": "Itálico",
    "merge": "Unir células",
    "mergeButtons": {
      "mergeCells": "Unir tudo",
      "mergeHorizontally": "Unir horizontalmente",
      "mergeVertically": "Unir verticalmente",
      "unmerge": "Separar"
    },
    "open": "Abrir...",
    "paste": "Colar",
    "quickAccess": {
      "redo": "Refazer",
      "undo": "Desfazer"
    },
    "saveAs": "Guardar como...",
    "sortAsc": "Ordenar ascendente",
    "sortDesc": "Ordenar descendente",
    "sortButtons": {
      "sortSheetAsc": "Ordenar folha de A a Z",
      "sortSheetDesc": "Ordenar folha de Z a A",
      "sortRangeAsc": "Ordenar intervalo de A a Z",
      "sortRangeDesc": "Ordenar intervalo de Z a A"
    },
    "textColor": "Cor do texto",
    "textWrap": "Quebrar texto",
    "underline": "Sublinhado",
    "validation": "Validação de dados..."
  });
}

if (kendo.spreadsheet && kendo.spreadsheet.messages.view) {
  kendo.spreadsheet.messages.view =
  $.extend(true, kendo.spreadsheet.messages.view,{
    "errors": {
      "shiftingNonblankCells": "Não é possível inserir células devido à possibilidade de perda de dados. Selecione outra localização para inserção ou elimine os dados do final da sua folha de cálculo.",
      "filterRangeContainingMerges": "Não é possível criar um filtro dentro de um intervalo que contenha fusões",
      "validationError": "O valor que inseriu viola as regras de validação definidas na célula."
    },
    "tabs": {
      "home": "Início",
      "insert": "Inserir",
      "data": "Dados"
    }
  });
}

/* Mensagens do Slider */

if (kendo.ui.Slider) {
  kendo.ui.Slider.prototype.options =
  $.extend(true, kendo.ui.Slider.prototype.options,{
    "increaseButtonTitle": "Aumentar",
    "decreaseButtonTitle": "Diminuir"
  });
}

/* Mensagens do ListBox */

if (kendo.ui.ListBox) {
  kendo.ui.ListBox.prototype.options.messages =
  $.extend(true, kendo.ui.ListBox.prototype.options.messages,{
    "tools": {
      "remove": "Eliminar",
      "moveUp": "Mover para cima",
      "moveDown": "Mover para baixo",
      "transferTo": "Transferir para",
      "transferFrom": "Transferir de",
      "transferAllTo": "Transferir tudo para",
      "transferAllFrom": "Transferir tudo de"
    }
  });
}

/* Mensagens do TreeList */

if (kendo.ui.TreeList) {
  kendo.ui.TreeList.prototype.options.messages =
  $.extend(true, kendo.ui.TreeList.prototype.options.messages,{
    "noRows": "Sem registos para mostrar",
    "loading": "A carregar...",
    "requestFailed": "Pedido falhou.",
    "retry": "Tentar novamente",
    "commands": {
        "edit": "Editar",
        "update": "Atualizar",
        "canceledit": "Cancelar",
        "create": "Adicionar novo registo",
        "createchild": "Adicionar registo filho",
        "destroy": "Eliminar",
        "excel": "Exportar para Excel",
        "pdf": "Exportar para PDF"
    }
  });
}

/* Mensagens do TreeView */

if (kendo.ui.TreeView) {
  kendo.ui.TreeView.prototype.options.messages =
  $.extend(true, kendo.ui.TreeView.prototype.options.messages,{
    "loading": "A carregar...",
    "requestFailed": "Pedido falhou.",
    "retry": "Tentar novamente"
  });
}

/* Mensagens do Upload */

if (kendo.ui.Upload) {
  kendo.ui.Upload.prototype.options.localization =
  $.extend(true, kendo.ui.Upload.prototype.options.localization,{
    "select": "Selecionar ficheiros...",
    "cancel": "Cancelar",
    "retry": "Tentar novamente",
    "remove": "Remover",
    "clearSelectedFiles": "Limpar",
    "uploadSelectedFiles": "Enviar ficheiros",
    "dropFilesHere": "Arraste os ficheiros aqui para enviar",
    "statusUploading": "a enviar",
    "statusUploaded": "enviado",
    "statusWarning": "aviso",
    "statusFailed": "falhou",
    "headerStatusPaused": "Pausado",
    "headerStatusUploading": "A enviar...",
    "headerStatusUploaded": "Concluído",
    "uploadSuccess": "Ficheiro(s) enviado(s) com sucesso.",
    "uploadFail": "Falha ao enviar ficheiro(s).",
    "invalidMaxFileSize": "Tamanho do ficheiro demasiado grande.",
    "invalidMinFileSize": "Tamanho do ficheiro demasiado pequeno.",
    "invalidFileExtension": "Tipo de ficheiro não permitido."
  });
}

/* Mensagens do Validator */

if (kendo.ui.Validator) {
  kendo.ui.Validator.prototype.options.messages =
  $.extend(true, kendo.ui.Validator.prototype.options.messages,{
    "required": "{0} é obrigatório",
    "pattern": "{0} não é válido",
    "min": "{0} deve ser maior ou igual a {1}",
    "max": "{0} deve ser menor ou igual a {1}",
    "step": "{0} não é válido",
    "email": "{0} não é um email válido",
    "url": "{0} não é uma URL válida",
    "date": "{0} não é uma data válida",
    "dateCompare": "A data final deve ser maior ou igual à data de início"
  });
}

/* Método kendo.ui.progress */
if (kendo.ui.progress) {
  kendo.ui.progress.messages =
  $.extend(true, kendo.ui.progress.messages, {
      loading: "A carregar..."
  });
}

/* Diálogo */

if (kendo.ui.Dialog) {
  kendo.ui.Dialog.prototype.options.messages =
  $.extend(true, kendo.ui.Dialog.prototype.options.localization, {
    "close": "Fechar"
  });
}

/* TimePicker */

if (kendo.ui.TimePicker) {
  kendo.ui.TimePicker.prototype.options.messages =
  $.extend(true, kendo.ui.TimePicker.prototype.options.messages, {
      set: "Definir",
      cancel: "Cancelar",
      hour: "hora",
      minute: "minuto",
      second: "segundo",
      millisecond: "milissegundo",
      now: "Agora"
  });
}

/* DateTimePicker */

if (kendo.ui.DateTimePicker) {
  kendo.ui.DateTimePicker.prototype.options.messages =
  $.extend(true, kendo.ui.DateTimePicker.prototype.options.messages, {
      set: "Definir",
      cancel: "Cancelar",
      hour: "hora",
      minute: "minuto",
      second: "segundo",
      millisecond: "milissegundo",
      now: "Agora",
      date: "Data",
      time: "Hora",
      today: "Hoje",
      weekColumnHeader: ""
  });
}


  /* Calendário */
if (kendo.ui.Calendar) {
  kendo.ui.Calendar.prototype.options.messages =
  $.extend(true, kendo.ui.Calendar.prototype.options.messages, {
      "today": "Hoje",
      "weekColumnHeader": "",
      "navigateTo": "Navegar para ",
      "parentViews": {
          "month": "vista anual",
          "year": "vista de década",
          "decade": "vista de século"
      }
  });
}

/* Alerta */
if (kendo.ui.Alert) {
  kendo.ui.Alert.prototype.options.messages =
  $.extend(true, kendo.ui.Alert.prototype.options.localization, {
    "okText": "OK"
  });
}

/* Confirmar */
if (kendo.ui.Confirm) {
  kendo.ui.Confirm.prototype.options.messages =
  $.extend(true, kendo.ui.Confirm.prototype.options.localization, {
    "okText": "OK",
    "cancel": "Cancelar"
  });
}

/* Prompt */
if (kendo.ui.Prompt) {
  kendo.ui.Prompt.prototype.options.messages =
  $.extend(true, kendo.ui.Prompt.prototype.options.localization, {
    "okText": "OK",
    "cancel": "Cancelar"
  });
}

/* DateInput */
if (kendo.ui.DateInput) {
  kendo.ui.DateInput.prototype.options.messages =
    $.extend(true, kendo.ui.DateInput.prototype.options.messages, {
      "year": "ano",
      "month": "mês",
      "day": "dia",
      "weekday": "dia da semana",
      "hour": "horas",
      "minute": "minutos",
      "second": "segundos",
      "dayperiod": "AM/PM"
    });
}

/* Mensagens da Lista */
if (kendo.ui.List) {
  kendo.ui.List.prototype.options.messages =
  $.extend(true, kendo.ui.List.prototype.options.messages,{
    "clear": "limpar",
    "noData": "Nenhum dado encontrado."
  });
}

/* Mensagens da DropDownList */
if (kendo.ui.DropDownList) {
  kendo.ui.DropDownList.prototype.options.messages =
  $.extend(true, kendo.ui.DropDownList.prototype.options.messages, kendo.ui.List.prototype.options.messages);
}

/* Mensagens da ComboBox */
if (kendo.ui.ComboBox) {
  kendo.ui.ComboBox.prototype.options.messages =
  $.extend(true, kendo.ui.ComboBox.prototype.options.messages, kendo.ui.List.prototype.options.messages);
}

/* Mensagens do AutoComplete */
if (kendo.ui.AutoComplete) {
  kendo.ui.AutoComplete.prototype.options.messages =
  $.extend(true, kendo.ui.AutoComplete.prototype.options.messages, kendo.ui.List.prototype.options.messages);
}

/* Mensagens do MultiColumnComboBox */
if (kendo.ui.MultiColumnComboBox) {
  kendo.ui.MultiColumnComboBox.prototype.options.messages =
  $.extend(true, kendo.ui.MultiColumnComboBox.prototype.options.messages, kendo.ui.List.prototype.options.messages);
}

/* Mensagens do DropDownTree */
if (kendo.ui.DropDownTree) {
  kendo.ui.DropDownTree.prototype.options.messages =
  $.extend(true, kendo.ui.DropDownTree.prototype.options.messages,{
      "singleTag": "item(s) selecionado(s)",
      "clear": "limpar",
      "deleteTag": "eliminar",
      "noData": "Nenhum dado encontrado."
  });
}

/* Mensagens do MultiSelect */
if (kendo.ui.MultiSelect) {
  kendo.ui.MultiSelect.prototype.options.messages =
  $.extend(true, kendo.ui.MultiSelect.prototype.options.messages,{
      "singleTag": "item(s) selecionado(s)",
      "clear": "limpar",
      "deleteTag": "eliminar",
      "noData": "Nenhum dado encontrado.",
      "downArrow": "Selecionar"
  });
}

/* Mensagens do Chat */
if (kendo.ui.Chat) {
  kendo.ui.Chat.prototype.options.messages =
  $.extend(true, kendo.ui.Chat.prototype.options.messages,{
      "messageListLabel": "Lista de mensagens",
      "placeholder": "Digite uma mensagem...",
      "toggleButton": "Alternar barra de ferramentas",
      "sendButton": "Enviar mensagem"
  });
}

/* Mensagens do Wizard */
if (kendo.ui.Wizard) {
  kendo.ui.Wizard.prototype.options.messages =
  $.extend(true, kendo.ui.Wizard.prototype.options.messages,{
      "reset": "Reiniciar",
      "previous": "Anterior",
      "next": "Próximo",
      "done": "Concluído",
      "step": "Passo",
      "of": "de"
  });
}

/* Mensagens do PDFViewer */
if (kendo.ui.PDFViewer) {
  kendo.ui.PDFViewer.prototype.options.messages =
  $.extend(true, kendo.ui.PDFViewer.prototype.options.messages, {
      defaultFileName: "Documento",
      toolbar: {
          zoom: {
              zoomLevel: "nível de zoom",
              zoomOut: "Diminuir Zoom",
              zoomIn: "Aumentar Zoom",
              actualWidth: "Largura Real",
              autoWidth: "Largura Automática",
              fitToWidth: "Ajustar à Largura",
              fitToPage: "Ajustar à Página"
          },
          open: "Abrir",
          exportAs: "Exportar",
          download: "Download",
          pager: {
              first: "Ir para a primeira página",
              previous: "Ir para a página anterior",
              next: "Ir para a próxima página",
              last: "Ir para a última página",
              of: "de",
              page: "página",
              pages: "páginas"
          },
          print: "Imprimir",
          toggleSelection: "Habilitar Seleção",
          togglePan: "Habilitar Panorâmica",
          search: "Pesquisar"
      },
      errorMessages: {
          notSupported: "Apenas são permitidos ficheiros PDF.",
          parseError: "Erro no processamento do ficheiro PDF.",
          notFound: "Ficheiro não encontrado.",
          popupBlocked: "Pop-up bloqueado."
      },
      dialogs: {
          exportAsDialog: {
              title: "Exportar...",
              defaultFileName: "Documento",
              pdf: "Formato de Documento Portátil (.pdf)",
              png: "Gráficos de Rede Portáteis (.png)",
              svg: "Gráficos Vetoriais Escaláveis (.svg)",
              labels: {
                  fileName: "Nome do ficheiro",
                  saveAsType: "Guardar como",
                  page: "Página"
              }
          },
          okText: "OK",
          save: "Guardar",
          cancel: "Cancelar",
          search: {
              inputLabel: "Texto de Pesquisa",
              matchCase: "Correspondência Maiúsculas/Minúsculas",
              next: "Próxima Correspondência",
              previous: "Correspondência Anterior",
              close: "Fechar",
              of: "de",
              dragHandle: "Arrastar pesquisa"
          }
      }
  });
}

/* Mensagens do Captcha */
if (kendo.ui.Captcha) {
  kendo.ui.Captcha.prototype.options.messages =
  $.extend(true, kendo.ui.Captcha.prototype.options.messages,{
      "reset": "Reiniciar captcha",
      "audio": "Reproduzir captcha",
      "imageAlt": "Digite o código Captcha da imagem",
      "success": "Verificação bem-sucedida"
  });
}

/* Mensagens do OrgChart */
if (kendo.ui.OrgChart) {
  kendo.ui.OrgChart.prototype.options.messages =
  $.extend(true, kendo.ui.OrgChart.prototype.options.messages,{
      label: "Organograma",
      edit: "Editar",
      create: "Criar",
      destroy: "Eliminar",
      destroyContent: "Tem a certeza de que deseja eliminar este item e todos os seus filhos?",
      destroyTitle: "Eliminar item",
      cancel: "Cancelar",
      save: "Guardar",
      menuLabel: "Menu de Edição",
      uploadAvatar: "Carregar novo avatar",
      parent: "Pai",
      name: "Nome",
      title: "Título",
      none: "--Nenhum--",
      expand: "expandir",
      collapse: "recolher"
  });
}

/* Mensagens do Mapa */
if (kendo.dataviz.ui.Map) {
  kendo.dataviz.ui.Map.prototype.options.messages =
  $.extend(true, kendo.dataviz.ui.Map.prototype.options.messages, {
      "tileTitle": "Título do Mapa"
  });
}

})(window.kendo.jQuery);


}));

kendo.culture("pt-PT");

