-- ========================
-- General Settings
-- ========================
-- Shorten vim.opt for convenience
local opt = vim.opt

-- Basic Settings
opt.number = true               -- Show line numbers
opt.relativenumber = true       -- Show relative line numbers
opt.tabstop = 4                 -- Tab size of 4 spaces
opt.shiftwidth = 4              -- Indent size
opt.expandtab = true            -- Use spaces instead of tabs
opt.smartindent = true          -- Smart indentation
opt.wrap = false                -- Disable line wrap
opt.cursorline = true           -- Highlight the current line
opt.termguicolors = true        -- Enable 24-bit colors
opt.splitright = true           -- Vertical splits open to the right
opt.splitbelow = true           -- Horizontal splits open below
opt.scrolloff = 8               -- Keep cursor 8 lines away from edges
--opt.background = "dark"

-- Disable swap and backup files
opt.swapfile = false
opt.backup = false
opt.undofile = true             -- Enable persistent undo

-- Search Settings
opt.ignorecase = true           -- Case-insensitive search
opt.smartcase = true            -- Case-sensitive if uppercase is used
opt.hlsearch = false            -- Don't highlight search results
opt.incsearch = true            -- Incremental search

-- ========================
-- Plugin Management (Packer)
-- ========================
-- Ensure packer is installed
local ensure_packer = function()
    local fn = vim.fn
    local install_path = fn.stdpath("data") .. "/site/pack/packer/start/packer.nvim"
    if fn.empty(fn.glob(install_path)) > 0 then
        fn.system({"git", "clone", "--depth", "1", "https://github.com/wbthomason/packer.nvim", install_path})
        vim.cmd([[packadd packer.nvim]])
        return true
    end
    return false
end
local packer_bootstrap = ensure_packer()

-- Packer Configuration
require("packer").startup(function(use)
    -- Plugin Manager
    use("wbthomason/packer.nvim")

    -- Appearance
    use("sainnhe/everforest")
    use("rebelot/kanagawa.nvim")
    use("nvim-lualine/lualine.nvim")       -- Statusline
    use("kyazdani42/nvim-web-devicons")    -- Icons

    -- File Navigation
    use("nvim-tree/nvim-tree.lua")         -- File explorer
    use("nvim-telescope/telescope.nvim")   -- Fuzzy finder
    use("nvim-lua/plenary.nvim")           -- Dependency for telescope

    -- Coding Enhancements
    use("neovim/nvim-lspconfig")           -- LSP support
    use("hrsh7th/nvim-cmp")                -- Completion engine
    use("hrsh7th/cmp-nvim-lsp")            -- LSP completion source
    use("L3MON4D3/LuaSnip")                -- Snippet engine
    use("saadparwaiz1/cmp_luasnip")        -- Snippet completions
    use("nvim-treesitter/nvim-treesitter") -- Syntax highlighting

    -- Git Integration
    use("tpope/vim-fugitive")              -- Git commands
    use("lewis6991/gitsigns.nvim")         -- Git signs in the gutter

    -- Automatically sync plugins if packer was just installed
    if packer_bootstrap then
        require("packer").sync()
    end
end)

-- ========================
-- Key Mappings
-- ========================
local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }

-- Leader Key
vim.g.mapleader = " "

-- General Key Mappings
-- Keybinding for toggling NvimTree
vim.api.nvim_set_keymap('n', '<leader>e', ':NvimTreeToggle<CR>', { noremap = true, silent = true })

map("n", "<leader>ff", ":Telescope find_files<CR>", opts) -- Find files
map("n", "<leader>fg", ":Telescope live_grep<CR>", opts)  -- Live grep
map("n", "<leader>fb", ":Telescope buffers<CR>", opts)    -- Buffers list


-- Better Navigation
map("n", "<C-h>", "<C-w>h", opts)
map("n", "<C-j>", "<C-w>j", opts)
map("n", "<C-k>", "<C-w>k", opts)
map("n", "<C-l>", "<C-w>l", opts)

-- ========================
-- Plugin Configurations
-- ========================

-- colorscheme Theme
vim.cmd([[colorscheme everforest]])

vim.g.everforest_background = 'medium'  -- Options: 'light', 'medium', 'dark'
vim.g.everforest_enable_italic = 1      -- Enable italic for comments, functions, etc.
vim.g.everforest_ui_contrast = 'high'   -- Options: 'low'


vim.env.PATH = "/home/danny/.nvm/versions/node/v18.20.5/bin:" .. vim.env.PATH


-- Lualine
require("lualine").setup({
    options = { theme = "everforest" },
})

-- ========================
-- Nvim-Tree Configuration
-- ========================
require("nvim-tree").setup({
    --auto_close = true,            -- Close the tree when it's the last window
    auto_reload_on_write = true,  -- Automatically reload when files are modified outside        -- Don’t open on startup
    update_cwd = true,            -- Update the current working directory to the directory of the file opened
    view = {
        width = 30,               -- Width of the tree
        side = "left",            -- Position of the tree
    },
})
vim.api.nvim_set_keymap('n', '<leader>q', ':NvimTreeClose<CR>', { noremap = true, silent = true })


-- Gitsigns

-- Treesitter
require("nvim-treesitter.configs").setup({
    ensure_installed = "all",  -- Install all maintained parsers
    highlight = {
        enable = true,                 -- Enable Treesitter-based highlighting
        disable = {},                  -- Disable specific languages (e.g., {"html"})
    },
    incremental_selection = {
        enable = true,                 -- Enable incremental selection
        keymaps = {
            init_selection = "<CR>",    -- Start selection with Enter
            node_incremental = "<Tab>", -- Increment selection
            scope_incremental = "<S-Tab>", -- Increment scope selection
            node_decremental = "<C-CR>", -- Decrement selection
        },
    },
    textobjects = {
        select = {
            enable = true,
            lookahead = true,
            keymaps = {
                -- Key mappings for selecting text objects
                ["af"] = "@function.outer",   -- Select the whole function
                ["if"] = "@function.inner",   -- Select the inner part of the function
                ["ac"] = "@class.outer",      -- Select the whole class
                ["ic"] = "@class.inner",      -- Select the inner part of the class
            },
        },
    },
    indent = {
        enable = true,  -- Enable Tree-sitter-based indentation
    },
})



-- LSP (Language Server Protocol)
local lspconfig = require("lspconfig")
lspconfig["pyright"].setup({
    cmd = { '/home/danny/.nvm/versions/node/v18.20.5/bin/pyright-langserver', '--stdio' }
}) -- Example: Python LSP
lspconfig["ts_ls"].setup({}) -- Example: JavaScript/TypeScript LSP



-- Completion
local cmp = require("cmp")
cmp.setup({
    snippet = {
        expand = function(args)
            require("luasnip").lsp_expand(args.body)
        end,
    },
    mapping = {
        ["<C-Space>"] = cmp.mapping.complete(),
        ["<CR>"] = cmp.mapping.confirm({ select = true }),
    },
    sources = {
        { name = "nvim_lsp" },
        { name = "luasnip" },
    },
})

