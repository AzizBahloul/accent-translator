import * as vscode from 'vscode';

const DIALECTS = [
    'british',
    'australian',
    'southern-usa',
    'pirate',
    'scottish',
    'indian'
];

export class DialectSelector {
    async selectDialect(): Promise<string | undefined> {
        return await vscode.window.showQuickPick(DIALECTS, {
            placeHolder: 'Select target dialect',
            title: 'Accent Translator',
            ignoreFocusOut: true
        });
    }
}
