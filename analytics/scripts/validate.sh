#!/bin/bash

# Analytics Platform - テンプレート検証スクリプト
# CFN Lint + SAM validate を実行して品質を確保

set -e

echo "🔍 Analytics Platform テンプレート検証を開始..."

# CFN Lint実行
echo "📋 CFN Lint実行中..."
if cfn-lint template.yaml; then
    echo "✅ CFN Lint: 正常終了 (exit code 0)"
else
    echo "❌ CFN Lint: エラーが検出されました"
    exit 1
fi

# SAM validate実行
echo "🔧 SAM validate実行中..."
if sam validate --template template.yaml; then
    echo "✅ SAM validate: 正常終了"
else
    echo "❌ SAM validate: エラーが検出されました"
    exit 1
fi

echo "🎉 すべての検証が正常に完了しました！"
echo ""
echo "次のステップ:"
echo "  1. sam build でビルド"
echo "  2. sam deploy --guided でデプロイ"