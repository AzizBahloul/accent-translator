import * as vscode from 'vscode';
import { Translator } from './translator';
import { DialectSelector } from './ui/dialectSelector';
import { StatusBar } from './ui/statusBar';

export function activate(context: vscode.ExtensionContext) {
    const translator = new Translator();
    const statusBar = new StatusBar();
    const dialectSelector = new DialectSelector();
    
    statusBar.update('Ready');
    
    context.subscriptions.push(
        vscode.commands.registerCommand('accent-translator.translate', async () => {
            try {
                const editor = vscode.window.activeTextEditor;
                if (!editor) {
                    vscode.window.showWarningMessage('No active editor!');
                    return;
                }
                
                const dialect = await dialectSelector.selectDialect();
                if (!dialect) return;
                
                statusBar.update(`Translating to ${dialect}...`);
                
                await translator.translateActiveDocument(dialect);
                statusBar.update(`Translated to ${dialect}`);
                
            } catch (error) {
                vscode.window.showErrorMessage(`Translation failed: ${error}`);
                statusBar.update('Error');
            }
        })
    );
}

export function deactivate() {
    StatusBar.dispose();
}
